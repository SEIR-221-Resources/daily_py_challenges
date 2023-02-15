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

#Challenge: 30-bank_transactions
#Difficulty:  Intermediate
#Prompt:
#- Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. Write three methods to perform these calculations and output the result to the user. 

#Gather user input using the `input` function. Note that input always returns user input as a string. You have to manually convert it to an int or a float to make it behave like number. Also, end the input prompt with a \n newline character if you want the user to type in on the next line.

#```
#age = input("How old are you?\n")
#age = int(age)
#```

#Here is a sample output:

#```
#Your current balance is
#4000
#What would you like to do? (deposit, withdraw, check_balance)
#deposit
#How much would you like to deposit?
#1000
#Your current balance is 5000
#Are you done?
#yes
#Thank you!
#```

# Your solution for 30-bank_transactions here:

print("Welcome to Chase bank.")

should_run = True
balance = 0

while should_run:
    print("what would you like to do? (deposit, withdraw, check_balance)")
    prompt = '> '
    action = input(prompt)

    if action == "deposit":
        print("enter an amount")
        amount = int(input(prompt))
        balance += amount
    elif action == "withdraw":
        print("enter an amount")
        amount = int(input(prompt))
        balance -= amount
    elif action == "check_balance":
        print(f"your current balance is : {balance}")
    else:
        print("invalid input")

    print("are you done? ('y/n')")
    done = input(prompt)
    if done == "y":
        print("Have a nice day!")
        should_run = False