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
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    return a / b

prompt = input('What calculation would you like to do? (add, sub, mult, div): ').upper()
num1 = int(input('What is the first number? '))
num2 = int(input('What is the second number? '))

if prompt == 'ADD':
    print(f"Solution: {add(num1,num2)}")
elif prompt == 'SUB':
    print(f"Solution: {sub(num1,num2)}")
elif prompt == 'MULT':
    print(f"Solution: {mult(num1,num2)}")
elif prompt == 'DIV':
    print(f"Solution: {div(num1,num2)}")
else:
    print("Please enter a valid computation operation")
