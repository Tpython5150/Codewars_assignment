'''
1. Create a function that takes an integer as an argument and returns "Even" for even numbers or 
"Odd" for odd numbers.

'''
def even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
even_or_odd(1)
even_or_odd(2)
even_or_odd(3)
even_or_odd(4)

'''
2. We need a function that can transform a number (integer) into a string.
What ways of achieving this do you know?
'''
num = int(input("Enter a number: "))

def number_to_string(number):
    return  str(number)
print(number_to_string(num))

def number_to_string(number):
    return str(number)
print(number_to_string(2))
print(number_to_string(3))
print(number_to_string(4))
print(number_to_string(5))

'''
3. Count the number of vowels int the sentence I'm going to Disney World!
'''

sentence = "I'm going to Disney World!"

def vowel_count(sentence):
    vowels = "a,e,i,o,u"
    count = 0
    for char in sentence:
        if char.lower() in vowels:
            count += 1
    return count
print(vowel_count(sentence))