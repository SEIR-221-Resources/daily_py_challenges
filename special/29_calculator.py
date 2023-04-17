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

prompt = '> '
print("Enter a type of math: add, sub, mult, div")
math = input(prompt)

print("Enter the first number")
num_one = int(input(prompt))
print("Enter the second number")
num_two = int(input(prompt))

print(f"input user data: math {math}, num 1 {num_one}, num 2 {num_two}")

operations = {
    "add": num_one + num_two,
    "sub": num_one - num_two,
    "mult": num_one * num_two,
    "div": num_one * num_two
}

if math in operations:
    print(f"result {operations[math]}")
else:{f"{math} is not a valid math"}
