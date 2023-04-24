

# #Challenge: 21-shortest_word
# #Difficulty:  Intermediate
# #Prompt:
# #- Write a function called shortest_word that accepts a single string as argument.
# #- The shortest_word function should return the length of the shortest word(s). String will never be empty, and you do not need to account for different data types.
# #Example:
# #shortest_word("I don't think that word means what you think it means") // => '1'

# # Your solution for 21-shortest_word here:

def shortest_word(s): 
    words = s.split(' ')

    word_length = []
    for word in words:
        word_length.append(len(word))

    return min(word_length)

shortest_word_string="I don't think that word means what you think it means"
print(f'shortest_word solution: \n > {shortest_word(shortest_word_string)}')



# #Challenge: 22-reverse_a_string
# #Difficulty:  Intermediate
# #Prompt:
# #- Reverse a string manually. Don't use s[::-1] (even though that's awesome). Create a new variable storing an empty string and add the letters from the first string one by one. The for loop should iterate over the length of the string and you should access letters individually.

# #Hint:
# ## Python offers several ways to reverse a String. This is a classic thing that lots of people want to do. It's probably easy to look up this answer on Stack Overflow.

# # Your solution for 22-reverse_a_string here:

def reverse_a_string(string):
    
    new_string = ''

    new_string_array = list(reversed(string))

    for character in new_string_array:
        new_string += character
    return new_string

# # list(test_string)
# for character in list(reversed(test_string)):
#     char = new_string_array.pop() 
#     new_string += char

# print(new_string)

backwards_string="snaem ti kniht uoy tahw snaem drow taht kniht t'nod I"
print(f'reverse_a_string solution: \n > {reverse_a_string(backwards_string)} = {shortest_word_string}')

# #Challenge: 23-shortest_word
# #Difficulty:  Intermediate
# #Prompt:
# #- Write a function called sum_of_minimums that accepts a single list as an argument.
# #- Given a 2D list of size m * n, your task is to find the sum of the minimum value in each row.
# #- You will always be given non-empty lists containing positive values.

# # Your solution for 23-sum_of_minimums here:


#NOTE: here

def sum_of_minimums(list):
    check = list[0]
    
    
    pivot = list[-1]
    left = [num for num in list[:-1] if num <= pivot]
    right = [num for num in list[:-1] if num > pivot]
    if left == []:
        lowest_2 = pivot + right[0]
        
        return lowest_2
    elif len(left) == 1:
        lowest_2 = left[0] + pivot
        
        return lowest_2
    else:
        return sum_of_minimums(left)


# print(sum_of_minimums([1, 3, 3, 4, 5, 0, 7, 24, ]))

    

my_list = [ [1,2,3,4,5], [5,6,7,8,9], [20,21,34,56,100] ]
print(f'sum_of_minimums solution: \n > {sum_of_minimums(my_list)} = 26')

# #Challenge: 24-palindrome_number
# #Difficulty:  Basic
# #Prompt:
# #- Write a function called palindrome_number that, given an integer x, return true if x is a palindrome, and false otherwise.

# # Your solution for 24-palindrome_number:

def palindrome_number(num):
    mun = list(str(num))
    mun.reverse()
    number = int(''.join(mun))
    if num == number:
        return True
    else:
        return False


print(f'is_palindrome solution: \n > {palindrome_number(101)} = True \n > {palindrome_number(10)} = False')

# #Challenge: 25-fizz_buzz
# #Difficulty:  Basic
# #Prompt:
# #- Write a function called fizz_buzz that, given an integer n, return a string array answer (1-indexed) where:

# #answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# #answer[i] == "Fizz" if i is divisible by 3.
# #answer[i] == "Buzz" if i is divisible by 5.
# #answer[i] == i (as a string) if none of the above conditions are true.

# #Example:
# #Input: n = 15
# #Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

# # Your solution for 25-fizz_buzz:

def fizz_buzz(n):
    for number in range(n+1):
        if n%3 == 0 and n%5 == 0:
            return('Fizzbuzz')
        elif n%3 == 0:
            return('Fizz')
        elif n%5 == 0:
            return('Buzz')
        else:
            return(n)


n=15
fizz_buzz_res=['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
print(f'fizz_buzz solution: \n > {fizz_buzz(n)} \n > = \n > {fizz_buzz_res}')

# #Challenge: 26-alphabetical
# #Difficulty:  Intermediate
# #Prompt:
# #- Create a function that takes a string and returns the string with the letters in alphabetical order (ie. `hello` becomes `ehllo`), Assume numbers and punctuation symbols will not be included in the string.

# #```
# #Give me a string to alphabetize
# #supercalifragilisticexpialidocious
# #Alphabetized: aaacccdeefgiiiiiiillloopprrssstuux
# #```

# #Hint:
# ## You'll need to use a couple of built in functions to alphabetize a string. 
# # Try to avoid looking up the exact answer and look at built in functions for lists and strings instead.

# # Your solution for 26-alphabetical here:

def alphabetical(s): 
    chars = list(s)
    def chars_sort_key(c):
        # ord() returns a unicode value for the character
        return ord(c)
    sorted_chars = sorted(chars, key=chars_sort_key)
    
    joined = ''.join(sorted_chars)
    return joined
    # for char in list:



word = 'supercalifragilisticexpialicosious'
print(f'alphabetical solution: \n > {alphabetical(word)} = aaaccceefgiiiiiiillloopprrsssstuux')

# #Challenge: 27-two_sum
# #Difficulty:  Intermediate
# #Prompt:
# #- Write a function called two_sum that given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# #You may assume that each input would have exactly one solution, and you may not use the same element twice.

# #You can return the answer in any order.

# #Example:
# #Input: nums = [2,7,11,15], target = 9
# #Output: [0,1]
# #Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# # Your solution for 27-two_sum here:

# #NOTE: here

def two_sum(nums, target):
    return 'didnt finish'
    # for index, num in enumerate(nums):
        
        # accumulator = 0
        # recurse = True
        # def func(acc, check_recurse):
        #     if nums[index] + nums[acc] == target:
        #         list = [index, acc]
        #         global recurse
        #         global accumulator
        #         accumulator = 1
        #         recurse = False
        #         return list
        #     else:
        #         acc +=1
        #     while check_recurse == True:
        #         func(acc, check_recurse)
        # func(accumulator, recurse)

    # Will return an array of index values 
    
                
nums=[2,7,11,15]
target=9
print(f'two_sum solution: \n > {two_sum(nums, target)} = [0, 1]')

# #Challenge: 28-roman_to_integer
# #Difficulty:  Intermediate
# #Prompt:
# #- Write a function called roman_to_int that, given a Roman numeral, convert it to an integer.

# #- https://en.wikipedia.org/wiki/Roman_numerals

# #Example 1:
# #Input: s = "III"
# #Output: 3
# #Explanation: III = 3.

# #Example 2:
# #Input: s = "LVIII"
# #Output: 58
# #Explanation: L = 50, V= 5, III = 3.

# # Your solution for 28-roman_to_integer here:

# logic:
    # if index is not next to an I, you just read the number
    # if it is next to an I, then:
        # figure out how many Is are before or after the number, cache those
        # 

def roman_to_int(s):
    i = 1
    v = 5
    x = 10
    l = 50
    cache = []
    for char in s:
        char = char.lower()
        if char == 'i':
            cache.append(i)
        elif char == 'v':
            cache.append(v)
        elif char == 'x':
            cache.append(x)
        elif char == 'l':
            cache.append(l)
    answer = sum(cache)
    print(f'answer: {answer}')
    return answer

# print(roman_to_ind('LVIII'))
		
r='LVIII'
print(f'roman_to_int solution: \n > {roman_to_int(r)} = 58')