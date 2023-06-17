# # Function - and activity that is natural to or the purpose of a person or thing.
# # Functions we've already seen
# # input(), len(), int(), print() #


# # name = input("What is your name?")
# # age = input("How old are you?")
# # if age > 18:
# #     print("Welcome")
# # else:
# #     print("You can not enter.")

# # We want to create two functions - one for name and one for age

# # Task seperation
# def ask_user_name():
#     # print("Now function is entered")
#     name = input("What is your name?")
#     # print(name)
#     return name # If you don't have this return the answer will not hold this value # You are in charge of what is returned
#     print("Hello") # Return means immediately exit this function, notice the print fades out

# # print("hello")
# answer = ask_user_name() 
# # print("hi")

# # Executes line 20, then line 17, then line 18, then line 22

# def ask_user_age():
#     age = input("How old are you?")
#     if age > 18:
#         print("Welcome")
#     else:
#         print("You can not enter.")

# # We need to define it, and then we need to call the function to execute the code underneath
# # The function definition needs to come before you can call it
# # Unless we call it, it doesn't get exectued

# # Function definition
# # Calling a function

# Parameters

# total = 0 # Global variable
# def add(number1, number2):
#     print(total)
#     result = number1 + number2 # This will add those two numbers and print the result  # Result is a local variable
#     return result

# answer = add(2,3) # This will assign 2 to number1, and 3 to number2
# print(answer) # Local variable

# If you need to use the calculation somehwere in your code be sure to use return

# Exercises

# Question 1
# Write a function called get_integer that takes a string as its argument, 
# and uses that string to prompt the user to enter an integer. 
# Your function should return the integer supplied by the user. Here's some starter code.
# prompt ="Could I please have an integer?:"
# Define your function here
# user_input = get_integer(prompt)
# print(f"So your integer is {user_input}? Thanks!")

# My Answer

prompt = input("Could I please have an integer?:")

def get_integer(x): #x = "Could I please have an interger?:""
    # result = int(input(x))
    # return result
    return int(input(x))

user_input = get_integer(prompt)
# get_integer("Give me something")
print(f"So your integer is {user_input}? Thanks!")

# Question 2

# Write a function called celcius_convert that takes a number representing thetemperature 
# in Farenheit as its argument, and returns a float representing the temperature in Celcius.
# Starter code:
# degrees_f = # Assign some number as the value here
# # Define your function here
# # print(celcius_convert(degrees_f))

# Not a function
# temperature = int(input("What is the temperature (Fahrenheit)? : "))
# print(f"Okay, so the temp in Fahrenheit is {temperature}...")
# answer = float((temperature-32)*5/9)
# print(f"Which means the temp in Celcius is {answer}")

# temperature = int(input("What is the temperature (Fahrenheit)? : "))
# print(f"Okay, so the temp in Fahrenheit is {temperature}...")
# def convert():
#     answer = float((temperature-32)*5/9)
#     print(f"Which means the temp in Celcius is {answer}")
# convert()