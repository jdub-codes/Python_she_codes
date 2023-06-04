# Store multiple data points, can take different data types
# digits = [1,2,3,4,5] #stri,int,float,list
# print(list_name)
# print(type(list_name))

# print(len(digits)) #This will give us the number of digits in the list

# Lists are index based which start from 0
# print(digits[5]) # This will give you an error because there is no number 6 - it doesn't exist
# print(digits[-1]) # Gives you the very last element
# print(digits[-2]) # Gives you the second last element

# # Slicing a list
# print(digits[0:4]) # Start (inclusive) and end (exclusive) index # This will return 1, 2, 3, 4
# print(digits [3:]) # This will return 4, 5 or
# # print(digits [-2:5]) This also works

# print(digits [0:5:2]) # :2 means skip the number in position two # 0:5 is exclusive

# digits = [1,2,3,4,5]
# print(digits)
# digits.append(6)
# print(digits) # This will add a six to the list
# digits.pop() # If you don't put anything inside it will just remove the last digit
# print(digits)

# digits = [1,2,3,4,5]
# print(digits)
# digits.append(6)
# print(digits) # This will add a six to the list
# digits.pop(0) # This will return 2, 3, 4, 5 and 6
# print(digits)

# digits = [1,2,3,4,5]
# print(digits)
# digits.append(6)
# print(digits) # This will add a six to the list
# popped_element = digits.pop(0) # This will store the digit for later
# print(popped_element) # This will return 1

# digits = [1,2,3,4,5]
# print(digits)
# digits.append(6)
# # print(digits) 
# popped_element = digits.pop(0) # This will store the digit for later
# # print(popped_element) 
# digits[1] = 90
# print(digits) #This will turn the second number into 90

# letters = ['a','b','c','d',['Emily','Julie']]
# print(letters[4][0]) # This will return Emily # Get from first list, then get the first element from another list

# # Check if 'a' exists in the list letters
# if 'a' in letters:
#     print("It is in the list")

# Exercises

# Question 1

# Given the list of foods below, print:
# The first item in the list.
# The third item in the list.
# The last item in the list.
# The first three items in the list.
# The last three items in the list.
# The last item in the sublist.

# foods = ["orange","apple","banana","strawberry","grape","blueberry", ["carrot", "cauliflower", "pumpkin"],"passionfruit","mango","kiwifruit"]

# print(foods[0])
# print(foods[2])
# print(foods[-1])
# print(foods[0:3])
# print(foods[7:]) # Nested lists count as one of the sequence of numbers
# print(foods[6][2]) # Carrot is number 6 in the index and pumpkin is in position 2

# Question 2

# # Format and print the contents of the following list so that the output appears
# A little bit of Monica in my life;
# A little bit of Erica by my side;
# A little bit of Rita's all I need;
# A little bit of Tina's what I see;
# A little bit of Sandra in the sun;
# A little bit of Mary having fun;
# A little bit of Jessica, here I am;
# A little bit of you makes me your man (ah!)
# *trumpet solo*

lyrics = [["Monica", "in my life"],["Erica", "by my side"],["Rita's", "all I need"],["Tina's", "what I see"],["Sandra", "in the sun"],["Mary", "having fun"],["Jessica", "here I am"]]

print("A little bit of",lyrics[0],";")
print("A little bit of you makes me your name (ah!)")
print("*trumpet solo*")

#Question 3

# Ask the user for three names. Add each name to a list, and then print the list.
# Anteres
# Rigel
# Arcturus
# ["Anteres", "Rigel", "Arcturus"]

# Firstname = input("Type the name Anterest")
# Secondname = input("Type the name Rigel")
# Thirdname = input("Type the name Arcturus")

# names = [Firstname, Secondname, Thirdname]
# print(names)

# Question 4

# Using the following starter code:
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
# d = []
# e = []

# Print the following lists:
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
# d = []
# e = []

# print(a, b, c)

# flatlist = (a + b + c)
# print(flatlist)
