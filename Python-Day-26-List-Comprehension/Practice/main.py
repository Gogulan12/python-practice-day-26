# #List comprehension
# numbers = [1, 2, 3]
# new_numbers = [n + 1 for n in numbers]
# name = "Gogulan"
# letters_list = [letter for letter in name]
#
# range_list = [num * 2 for num in range(1,5)]
#
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# long_names = [name.upper() for name in names if len(name) > 5]

######Exercise 1 - Squaring Numbers######
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# #Write your 1 line code 👇 below:
#
# squared_numbers = [ n * n for n in numbers]
#
# #Write your code 👆 above:
#
# print(squared_numbers)


######Exercise 2 - Data Overlap######

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# #Write your 1 line code 👇 below:
#
# result = [n for n in numbers if n % 2 == 0]
#
#
# #Write your code 👆 above:
#
# print(result)

######Exercise 3 - List Comprehension 3######
# with open("file1.txt") as file1:
#     file_1_data = file1.readlines()
#
# with open("file2.txt") as file2:
#     file_2_data = file2.readlines()
#
# result = [int(num) for num in file_1_data if num in file_2_data]
#
# # Write your code above 👆
#
# print(result)


######Dictionary Comprehension######
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
#
# students_scores = {student:random.randint(1, 100) for student in names}
#
# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}



######Exercise 4 - Dictionary Comprehension 1######
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# # Don't change code above 👆
#
# # Write your code below:
# result = {word:len(word) for word in sentence.split()}
#
#
# print(result)

######Exercise 5 - Dictionary Comprehension 2 ######
# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }
# # 🚨 Don't change code above 👆
#
#
# # Write your code 👇 below:
# weather_f = {day:(temp_c*9/5) + 32 for (day, temp_c) in weather_c.items()}
#
#
# print(weather_f)


#how to iterate over a pandas dataframe
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#loop through a data frame
for (key,value) in student_data_frame.items():
    print(key)


#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
    if row.student =="Angela":
        print(row.score)

#{new_key:new_value for (index, row) in df.iterrows()}


