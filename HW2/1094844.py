from pymongo import MongoClient
import pprint

client = MongoClient("mongodb+srv://1094844:homework@cluster0.xkp8kvk.mongodb.net/?retryWrites=true&w=majority")
db = client['homework']
collection = db['student_class_grade']

file1 = {"student_id": "s2", "student_name": "Rick", "class_id": "c1", "class_name": "Underwater basket weaving", "grade": "99"}
file2 = {"student_id": "s3", "student_name": "Susanna", "class_id": "c1", "class_name": "Underwater basket weaving", "grade": "65"}
file3 = {"student_id": "s4", "student_name": "Jennifer", "class_id": "c1", "class_name": "Underwater basket weaving", "grade": "3"}
file4 = {"student_id": "s2", "student_name": "Rick", "class_id": "c2", "class_name": "Home fusion made easy", "grade": "38"}
file5 = {"student_id": "s3", "student_name": "Susanna", "class_id": "c2", "class_name": "Home fusion made easy", "grade": "88"}
file6 = {"student_id": "s4", "student_name": "Jennifer", "class_id": "c2", "class_name": "Home fusion made easy", "grade": "48"}
file7 = {"student_id": "s1", "student_name": "Brett", "class_id": "c3", "class_name": "How to train an attack iguana", "grade": "7"}
file8 = {"student_id": "s4", "student_name": "Jennifer", "class_id": "c3", "class_name": "How to train an attack iguana", "grade": "32"}
file9 = {"student_id": "s1", "student_name": "Brett", "class_id": "c4", "class_name": "Learn SQL for fun and profit", "grade": "94"}
file10 = {"student_id": "s2", "student_name": "Rick", "class_id": "c4", "class_name": "Learn SQL for fun and profit", "grade": "63"}
file11 = {"student_id": "s3", "student_name": "Susanna", "class_id": "c4", "class_name": "Learn SQL for fun and profit", "grade": "75"}
file12 = {"student_id": "s4", "student_name": "Jennifer", "class_id": "c4", "class_name": "Learn SQL for fun and profit", "grade": "20"}

# Insert multiple files
# collection.insert_many([file1, file2, file3, file4, file5, file6, file7, file8, file9, file10, file11, file12])

print()

#Retrieve all data
print("Show all data in my MongoDB:")
all_data=collection.find()
for data in all_data:
    pprint.pprint(data)

print()

#Retrieve student_name who took the course name "Home fusion made easy"
print("Show the student_name who took the curse name 'Home fusion made easy': ")
students=collection.find({'class_name': 'Home fusion made easy'}, {"_id": 0, "student_name": 1})
for student_name in students:
    pprint.pprint(student_name)

print()

#Retrieve Jennifer's grade on the course named "Learn SQL for fun and profit"
print("Show Jennifer's grade on the course named 'Learn SQL for fun and profit': ")
Jennifer_grade=collection.find({'student_name': 'Jennifer', 'class_name': 'Learn SQL for fun and profit'}, {'_id': 0, 'grade': 1})
for grade in Jennifer_grade:
    pprint.pprint(grade)
