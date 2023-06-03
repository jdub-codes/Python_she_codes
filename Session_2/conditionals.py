# # Boolean
# name = "Asli"
# age = 19
# height = 1.5
# is_raining = True
# my_variable = False
# print(is_raining)
# print(type(my_variable))

# Boolean Expressions - Expressions that produce a boolean value in return
# Comparison Operators
# == is equal
# != is not equal
# > greater than
# < less than
# >= greater or equal to
# <= less than or equal to
# print(5 > 3)
# print(3.5> 6.3)
# print("Asli" == "Asli")

# # Mathematical Operators - Addition, Division, Subtraction, Multiplication
# # Boolean Operators - not, and, or
# is_sunny = True
# is_warm = True

# print(not is_sunny)
# print(is_sunny and is_warm)
# print(is_sunny or is_warm)

# answer = is_sunny or is_warm
# print(answer)
# print (True or True)
# print (False)

# temperature = 20
# # syntax (grammar) / semantics (logic) 
# if temperature <= 18:
#     print("Weather is too cold!")
#     print("I want to say home")
# elif temperature > 28: #if statement false it will check elif
#     print("Weather is too hot!")
# else:
#     print("Weather is nice!")

# multiple if statements, will check the expression regardless
# remember to indent

# else:
#     print("Weather is nice!")

# Sara is a confident rock climber, but sometimes she forgets her helmet. 
# Rei refuses to climb with Sara unless she's wearing a helmet, because That's Just Sensible.
# Write a program that sets the value for a boolean variable called sara_has_helmet, and then prints out a string indicating whether or not Rei is down to climb.
# sarah_has_helmet = True
# "Let's send it!")
# "No way, my brain is my moneymaker!"

# sarah_has_helmet = True

# if sarah_has_helmet:
#     print("Let's send it!")
# else:
#     print("No way, my brain is my moneymaker!")

# Rei is a very careful climber, but sometimes she is forgetful. 
# Even if Sara has a helmet,they still can't go climbing unless Rei remembers to bring her rope.
# sara_has_helmet = True
# rei_has_rope = True
# "Who's unprepared now, Rei?"
# "I guess let's just go hiking?"

# sarah_has_helmet = True
# rei_has_rope = True

# if sarah_has_helmet and rei_has_rope:
#     print("I guess let's just go hiking?")
# else:
#     print("Who's unprepared now, Rei?")

# sarah_has_helmet = True
# rei_has_rope = False

# if sarah_has_helmet and rei_has_rope:
#     print("I guess let's just go hiking?")
# else:
#     print("Who's unprepared now, Rei?")

# sarah_has_helmet = True
# rei_has_rope = False

# if sarah_has_helmet and rei_has_rope:
#     print("I guess let's just go hiking?")
# else:
#     print("Who's unprepared now, Rei?")

# sarah_has_helmet = False
# rei_has_rope = True

# if sarah_has_helmet and rei_has_rope:
#     print("I guess let's just go hiking?")
# else:
#     print("Who's unprepared now, Rei?") 

# sarah_has_helmet = False
# rei_has_rope = False

# if sarah_has_helmet and rei_has_rope:
#     print("Who's unprepared now, Rei?")
# else:
#     print("I guess let's just go hiking?")

# Write a program that implements the algorithm for red light cameras. 
# The program should print the string "Flash!" if (and only if) a car is detected driving while the light is red. 
# If the light is green or amber, the program should print "Do nothing.", evenwhen a car is detected.

light_color = "Red"
car_detected = False

if car_detected and light_color == "Red":
    print("Flash!")
else:
    print("Do nothing.")