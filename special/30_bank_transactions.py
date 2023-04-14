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

balance = int(input("At Niks bank we let you decide how rich you are, please let us know your balance: $  "))
display = input("What would you like to do? (deposit, withdraw, check_balance): ")

if display == "check_balance":
    print(f'your balance is {balance}')
elif display == "deposit":
    deposit = int(input("How much would you like to deposit?:$ "))
    new_amount = deposit + balance
    print(f'after your deposit of {deposit} your account has a balance of {new_amount}')
elif display == "withdraw":
    withdraw = int(input("How much would you like to withdraw?:$ "))
    new_amount = balance - withdraw
    print(f'after your deposit of {withdraw} your account has a balance of {new_amount}')
else:
   print("goodbye!")
