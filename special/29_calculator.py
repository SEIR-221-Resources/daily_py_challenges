#Challenge: 29-calculator
#Difficulty:  Intermediate
#Prompt:
#- Create a simple calculator that first prompts the user what method they would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the method with the two numbers. Here is a sample prompt:

#'''
#What calculation would you like to do? (add, sub, mult, div)
#add
#What is number 1?
#3
#What is number 2?
#6
#Your result is 9
#'''

#Hint:
# Use the `input()` function to prompt a user to enter something.
# input() always returns a string value. If you ever want someone
# to enter a number you have to use the `int()` function to convert
# what they typed in to a string.

# Your solution for 29-calculator here:
operation = input("What calculation would you like to do? (add, sub, mult, div) ").lower()
first = int(input("What is number 1? "))
second = int(input("What is number 2? "))

if operation == 'add':
    result = first + second
elif operation == 'sub':
    result = first - second
elif operation == 'mult':
    result = first * second
elif operation == 'div':
    result = first / second
    if result.is_integer():
        result = int(result)
else: 
    result = f"impossible to calculate because {operation} is not a valid operation."

print(f"Your result is {result}")