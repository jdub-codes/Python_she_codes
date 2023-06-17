import csv
# with open(file="dogs_are_awesome.csv", mode="r", encoding="utf-8") as my_file:
#     csv_reader = csv.reader(my_file, delimiter = " ")
#     for row in csv_reader:
#         print(row)


    # print(my_file) # cd to the correct directory e.g. Session_5
# open(file="dogs_are_awesome.csv") # only put the other things if you want to change it
# r is for reading 
# when you call a function the order of arguments are very important
# encoding gives the language for how it's been stored
# with helps us with opening external files
# my_file is arbitrary and this is the variable we will be referring to
# create a reader object e.g. my_file
# each row becomes a list # it will look to seperate by comma unless specify a delimiter

# with open(file="hello.csv", mode="w") as my_file:
#     csv_writer = csv.writer(my_file)
#     csv_writer.writerow("Hello", "Hi")

# creates a hello.csv file or it will overwrite it
# prints each string and separates it by a comma

# Exercises

# Question 1

# Write a program that reads in colours_20_simple.csv and print each line of the colour data one by one as a string. 
# Use spaces to separate the columns insead of commas.

with open(file="colours_20_simple.csv", mode="r", encoding="utf-8") as my_file:
    csv_reader = csv.reader(my_file, delimiter = " ")
    for row in csv_reader:
        print(row)



# Question 2 

# Write a program that reads in colours_20_simple.csv and outputs the colour data in order 
# English, Hex then RGB, like so:
# Green beige, Hex: #BEBD7F, RGB: 190-189-127

# My Answer

# Question 3

# Write a program that takes a csv file describing colours, 
# and outputs the number of times each of the following colours 
# appears in the English Name:redgreenblueyellowOutput for colours_20.csv:

# My Answer

# Question 4

# My Answer