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
balance = 3
def bank_transaction():
    global balance
    prompt = input(f'What would you like to do? (deposit, withdraw, check_balance) \n')
    prompt.lower()

    if prompt == 'deposit':
        depositPrompt = input(f'How much would you like to deposit? \n')
        depositAmount = int(depositPrompt)
        balance += depositAmount
        print(f'Your new balance is {balance}')
    if prompt == 'withdraw':
        withdrawResponse = input(f'How much would you like to withdraw? \n')
        withdrawAmount = int(withdrawResponse)
        balance -= withdrawAmount
        print(f'Your new balance is {balance} \n')
    if prompt == 'check_balance':
        print(f'Your balance is {balance}\n')
    

    prompt_leave = input(f'Would you like to perform another transaction? y/n \n')
    if prompt_leave.lower() == 'y':
        
        bank_transaction()
    

bank_transaction()
