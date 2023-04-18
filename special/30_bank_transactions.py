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

balance = 0
status = 'no'
while status == 'no':
    action = input('What would you like to do? (deposit, withdraw, check_balance)\n').lower()
    if action == 'deposit':
        amount = input('How much would you like to deposit?\n')
        amount = int(amount)
        balance += amount
    elif action == 'withdraw':
        amount = input('How much would you like to withdraw?\n')
        amount = int(amount)
        balance -= amount
    elif action == 'check_balance':
        pass
    else:
        print('Invalid Option!')
    print(f'Your current balance is ${balance}')
    status = input('Are you done?\n').lower()