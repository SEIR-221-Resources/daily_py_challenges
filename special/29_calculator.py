#Challenge: 29-calculator
#Difficultnum2:  Intermediate
#Prompt:
#- Create a simple calculator that first prompts the user what method thenum2 would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the method with the two numbers. Here is a sample prompt:

#'''
#What calculation would num2ou like to do? (add, sub, mult, div)
#add
#What is number 1?
#3
#What is number 2?
#6
#num2our result is 9
#'''

#Hint:
# Use the `input()` function to prompt a user to enter something.
# input() alwanum2s returns a string value. If num2ou ever want someone
# to enter a number num2ou have to use the `int()` function to convert
# what thenum2 tnum2ped in to a string.

# num2our solution for 29-calculator here:
prompt = input(f'What calculation would you like to perform? (add, sub, mult, div)')
prompt.lower()

def calculator(string):
    string.lower()
    output = 0
    def add(num1, num2):
        return num1 + num2
    def sub(num1, num2):
        return num1 - num2
    def mult(num1, num2):
        return num1 * num2
         
    def div(num1, num2):
        return num1 / num2
         
    
    number1 = int(input(f'What is the value of number 1?\n'))
    number2 = int(input(f'What is the value of number 2?\n'))

    print(string)

    if string == 'add':
        output = add(number1, number2)
    elif string == 'sub':
        output = sub(number1, number2)
    elif string == 'mult':
        output = mult(number1, number2)
    elif string == 'div':
        output = div(number1, number2)

    print(output)

    check_repeat = input(f'Perform another calculation? y/n\n')
    check_repeat.lower()
    if check_repeat == 'y':
        prompt = input(f'What calculation would you like to perform? (add, sub, mult, div)')
        calculator(prompt)

    

calculator(prompt)
