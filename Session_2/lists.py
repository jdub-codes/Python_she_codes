# Store multiple data points, can take different data types
digits = [1,2,3,4,5] #stri,int,float,list
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

letters = ['a','b','c','d',['Emily','Julie']]
print(letters[4][0]) # This will return Emily # Get from first list, then get the first element from another list

# Check if 'a' exists in the list letters
if 'a' in letters:
    print("It is in the list")


