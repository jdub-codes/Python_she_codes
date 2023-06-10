# Loops help us to perform a task multiple times

# letters = ['a','b','c']

# 2 types of loops
# While loops

# count = 0
# while 5 > count:
#     print("Hello") # You always want to make this false.
#     count = count + 1 # This means add 1 to the count. The loop will continue until it hits 5.

# count +- 1 # This is a lazy way of doing the same thing as above.

# name = input("What is your name?")
# while name !="Ashley":
#     print("I don't know you") # This will just print over and over again until the answer is Ashley.
#     name = input("Well, what's the new name?")

# For Loops

# letters = ['a','b','c']
# for letter in letters: # letter = 'a' after the loop the letter = 'b' and so forth
#     print(letter)

# list_name [0:10] range() is similar to slicing

# for number in range(0,10): # This works very similar to slicing. It will print every number from 0 to 10
#     print(number) # I want this to be done 10 times

# students = [
#     ["Cindy","Emily","Eve"],
#     ["Julie","Maddy","Andrea"],
#     ["Jenny","Sarah","Yara"]
#         ]
# # for student in students:
# #     print(student) # This will give you list, not the extracted values

# for student in students:
#     print(student) 
#     for name in student:
#         print(name)

# First we go inside the outer loop, then it will go inside the inner loop

# While loop exercises

# Continuously ask the user to enter a number until they provide a blank input. 
# Output the sum of all the numbers.

# My Answer

# number = input("Enter a number") # Ask the user for a number
# numberlist = [] # Put the number into a list 
# while number != '':
#     numberlist.append(int(number)) # This will add the number to the list # Change the string to a number using int
#     number = input("Enter a number") # Ask the user again for a number
#     print(numberlist)
# print(sum(numberlist))

#Question 2

# Ask the user to enter a integer number. 
# Print all the odd numbers between 0 and that number (inclusive). 
# (Its ok not to worry about negative numbers for now, unless you really want a challenge.)

# My Answer

# start = 0
# end = int(input("Enter a number"))
# for number in range (start, end + 1):
#     if number % 2 != 0:
#         print(number, end = " ")

# Question 3
# Write a guessing game. Select a number, and save it as a variable in your code.
# Ask the user to enter a number, and then output whether their number is less than or greater than the selected number. 
# Keep asking until the user guesses the correct number. Then print a congratulatatory message.

answer = 25
guess = int(input("Guess a number:"))
while guess == answer:
    if guess > answer:
        print("Too high...")
    elif guess < answer:
        print("Too low...")
    print("You got it right!")
