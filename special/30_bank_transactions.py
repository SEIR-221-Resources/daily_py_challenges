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
print("Welcome to Niks bank, remember we charge a button pressing fee everytime you use this application")
# What are things that we might need?
# Make a balance to start with
# What else needs to happen?
balance = int(input('Here at Niks bank we let you pick how rich you are, please input your starting balance > '))
# prompting the user for the next hting to do
# making the display lowercase (if it wasn't)

# A condition to loop
should_run = True

while should_run:

    display = input('What would you like to do? withdraw, deposit, check_balance? ')
    display.lower()
    if display == "deposit":
        deposit = int(input("How much would you like to deposit? "))
        balance += deposit
        print(f'Your new balance is... {balance} ')
    elif display == "withdraw":
        withdraw = int(input("How much would you like to withdraw? "))
        balance -= withdraw
        print(f'Your new balance is... {balance} ')
    else:
        print(f'The balance is {balance}')

    print("are you done yet?")
    done = input("Y/n ")
    if done == "y":
        print("Bye")
        should_run = False
