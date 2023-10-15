import math


# 1.Find The greatest common divisor of multiple numbers read from the console.
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def find_gcd_of_multiple_numbers(numbers_gcd):
    if len(numbers_gcd) < 2:
        return "At least two numbers are required to find the GCD."

    gcd = numbers_gcd[0]
    for i in range(1, len(numbers_gcd)):
        gcd = find_gcd(gcd, numbers_gcd[i])

    return gcd


try:
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers]

    result = find_gcd_of_multiple_numbers(numbers)
    print("The GCD of the numbers is:", result)
except ValueError:
    print("Invalid input. Please enter valid numbers separated by spaces.")


# 2.Write a script that calculates how many vowels are in a string.
def count_vowels(string):
    string = string.lower()

    vowels = "aeiou"

    count = 0

    for char in string:
        if char in vowels:
            count += 1

    return count


user_input = input("Enter a string: ")

vowel_count = count_vowels(user_input)
print("Number of vowels in the string:", vowel_count)


# 3.Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def count_occurrences(substring, full_string):
    count = 0
    start = 0
    while start < len(full_string):
        start = full_string.find(substring, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

occurrences = count_occurrences(string1, string2)
print("Number of occurrences:", occurrences)

# 4.Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
import re


def convert_to_lower_with_underscores(input_string):
    snake_case_string = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', input_string).lower()
    return snake_case_string


upper_camel_case_string = input("Enter a string in UpperCamelCase: ")

snake_case_string = convert_to_lower_with_underscores(upper_camel_case_string)
print("Converted string:", snake_case_string)


# 5.Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order

def spiral_order(matrix):
    result = []
    while matrix:
        result.extend(matrix[0])
        matrix = matrix[1:]

        if matrix and matrix[0]:
            for row in matrix:
                result.append(row[-1])
                row.pop()

        if matrix:
            result.extend(matrix[-1][::-1])
            matrix.pop()

        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row[0])
                row.pop(0)

    return ''.join(result)


matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

result = spiral_order(matrix)
print("Spiral order string:", result)


# 6.Write a function that validates if a number is a palindrome.
def is_palindrome(number):
    num_str = str(number)

    return num_str == num_str[::-1]


num = 121
if is_palindrome(num):
    print(f"{num} is a palindrome")
else:
    print(f"{num} is not a palindrome")

# 7.Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only the first number that is found.

import re


def extract_first_number(text):
    match = re.search(r'\d+', text)

    if match:
        number = int(match.group())
        return number
    else:
        return None


text1 = "An apple is 123 USD"
text2 = "abc123abc"

number1 = extract_first_number(text1)
number2 = extract_first_number(text2)

if number1 is not None:
    print(f"First number in text1: {number1}")
else:
    print("No number found in text1")

if number2 is not None:
    print(f"First number in text2: {number2}")
else:
    print("No number found in text2")


# 8.Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"
def count_ones_in_binary(number):
    binary_representation = bin(number)
    count_ones = binary_representation.count('1')
    return count_ones


num = 24
count = count_ones_in_binary(num)
print(f"The number {num} has {count} '1' bits in its binary representation.")


# 9.Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.
def most_common_letter(text_common_later):
    text_common = text_common_later.lower()

    char_count = {}

    for char in text_common:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    if not char_count:
        return None

    most_common = max(char_count, key=char_count.get)

    return most_common


text_common_later = "an apple is not a tomato"
common_char = most_common_letter(text_common_later)

if common_char is not None:
    print(f"The most common character in the text is '{common_char}'")
else:
    print("No letters found in the text")


# 10.Write a function that counts how many words exists in a text. A text is considered to be form out of words that are separated by only ONE space. For example: "I have Python exam" has 4 word
def count_words(text_count_words):
    words = text_count_words.split()
    return len(words)


text_count = "I have Python exam"
word_count = count_words(text_count)
print(f"The text contains {word_count} word(s).")
