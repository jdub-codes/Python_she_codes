# Lists
# numbers = [1,2,3]
# numbers[0] - tells the location, would return 1
# Dictionary - helps us store more than one value in one place
# Keys are unique
# Values can be any data type
# Keys can be only be immutable data types
# Immutable - Strings, integers, floats, booleans
# Curly brackets, it stores pairs,"Cindy" is the key, elements separated by a comma
# student_phonebook = {
#     "Cindy":111,
#     "Tracey":123,
#     "Pauline":444
#     } 

# print(student_phonebook)
# # # del student_phonebook["Tracey"] # This will delete Tracey
# # # student_phonebook["Cindy"] = 555 # This will overide Cindy's value
# # # print(student_phonebook["Asli"]) # This will give you an error
# # # student_phonebook["Yara"] = 555 # Square brackets are the new key
# # print(student_phonebook)
# # # print(type(student_phonebook))

# student_phonebook = {
#     "Cindy":111,
#     "Tracey":123,
#     "Pauline":444
#     } 

# for key in student_phonebook:
#     # print(element) # as a defeult it gives you the keys
#     print(key, student_phonebook[key]) # this is giving you pairs

# for value in student_phonebook.values(): # this will iterate through all of the values
#     print(value)

# a,b = [1,2]
# print(a)
# print(b)

# for example in student_phonebook.items():
#     print(example)

# for key,value in student_phonebook.items():
#     print(key,value)

# Exercises

# Question 1
# The dictionary below represents the cost of individual items in a supermarket. 
# Write a program that asks the user how many of each item they would like in turn, 
# and outputs the total cost of their groceries.

# My Answer
groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.10,
    "Coffee": 9.00,
    "Carrots": 0.56,
    "Oranges": 3.08
    }

grocerieslist = []
for quantity in range(0,6):
    number = input("How many of each item would you like?")
    grocerieslist.append(number)

for value in groceries.values():
    print(value)
    counter = 0
    print('{:.2f}'.format(int(grocerieslist[counter])*value))
    counter += 1

# Question 2

# In the last lesson, you wrote a program that counted the number of colour names 
# in the colours_865.csv file (available here).
# Try rewriting this program so that instead of using separate variables 
# to keep track of the number of times each colour name appears, 
# it uses a single dictionary instead. Here's a dictionary to get you started:

colour_counts = {
    "blue": 0,
    "green": 0,
    "yellow": 0,
    "red": 0,
    "purple": 0,
    "orange": 0,
    }


