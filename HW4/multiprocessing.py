import string, os
import multiprocessing
from collections import OrderedDict


def count_words(thread_number, lines, word_dict):
    for line in lines:
        line = line.translate(line.maketrans('', '', string.punctuation))  # Remove the punctuation marks from the line
        words = line.split(' ')  # Split the line into words

        # Iterate over each word in line
        for word in words:
            tuple_key = (thread_number, word)
            # Check if the word is already in dictionary
            if tuple_key in word_dict:
                word_dict[tuple_key] = word_dict[tuple_key] + 1  # Increment count of word by 1
            else:
                word_dict[tuple_key] = 1  # Add the word to dictionary with count 1


def main():
    manager = multiprocessing.Manager()
    word_dict = manager.dict()
    jobs = []

    with open('bible.txt', 'r') as f:
        file_size = os.stat('bible.txt')[6]
        processes = os.cpu_count()

        thread_number = 0
        while True:
            lines = [line.strip() for line in f.readlines(file_size // processes)]
            if not lines:
                break
            p = multiprocessing.Process(target=count_words, args=(thread_number, lines, word_dict))
            jobs.append(p)
            p.start()
            thread_number += 1

    for proc in jobs:
        proc.join()
    
    # merge the counts of word
    merge_word_dict = {}
    for key in word_dict:
        word = key[1]
        num = word_dict[key]
        if word in merge_word_dict:
            merge_word_dict[word] = merge_word_dict[word] + num
        else:
            merge_word_dict[word] = num
    
    # order word_dict by values and reverse the dictionary 
    order_word_dict = OrderedDict(sorted(merge_word_dict.items(), key=lambda x: x[1], reverse=True))

    # Print the contents of dictionary
    for key in list(order_word_dict.keys()):
        print(key, ":", order_word_dict[key])
        

if __name__ == "__main__":
    main()
