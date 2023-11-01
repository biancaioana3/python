# 1. Write a function to return a list of the first n numbers in the Fibonacci string.
def fibonacci(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


def get_primes(numbers):
    return [num for num in numbers if is_prime(num)]


# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)
def set_operations(a, b):
    intersection = list(set(a) & set(b))
    union = list(set(a) | set(b))
    difference_a = list(set(a) - set(b))
    difference_b = list(set(b) - set(a))
    return intersection, union, difference_a, difference_b


#  4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
def compose(notes, moves, start):
    song = []
    index = start
    for move in moves:
        song.append(notes[index])
        index = (index + move) % len(notes)
    return song


#   5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main.py diagonal with 0 (zero).
def replace_below_diagonal(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j] = 0
    return matrix


#  6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the items that appear exactly x times in the incoming lists.
from collections import Counter


def find_x_times_in_lists(x, *lists):
    counts = Counter(item for sublist in lists for item in sublist)
    return [item for item, count in counts.items() if count == x]


# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.
def is_palindrome(num):
    return str(num) == str(num)[::-1]


def find_palindromes(numbers):
    palindromes = [num for num in numbers if is_palindrome(num)]
    return len(palindromes), max(palindromes, default=None)


#  8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by x.
def ascii_divisibility(strings, x=1, flag=True):
    result = []
    for string in strings:
        if flag:
            result.append([char for char in string if ord(char) % x == 0])
        else:
            result.append([char for char in string if ord(char) % x != 0])
    return result


# 9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game. A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest row from the field.
def find_obstructed_seats(matrix):
    obstructed_seats = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i + 1, len(matrix)):
                if matrix[i][j] < matrix[k][j]:
                    obstructed_seats.append((i, j))
                    break
    return obstructed_seats


# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains the first items in the lists, the second element contains the items on the position 2 in the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")].
def group_lists(*lists):
    max_len = max(len(lst) for lst in lists)
    result = [tuple(lst[i] if i < len(lst) else None for lst in lists) for i in range(max_len)]
    return result


#  11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
def sort_tuple_list(tuples):
    return sorted(tuples, key=lambda x: x[1][2])


# 12. Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
def group_by_rhyme(words):
    rhyme_groups = {}
    for word in words:
        rhyme = word[-2:]
        if rhyme in rhyme_groups:
            rhyme_groups[rhyme].append(word)
        else:
            rhyme_groups[rhyme] = [word]
    return list(rhyme_groups.values())


# 1. Fibonacci
fib_sequence = fibonacci(10)
print("Fibonacci Sequence:", fib_sequence)

# 2. Prime Numbers
numbers = [2, 4, 7, 11, 15, 20, 23]
prime_numbers = get_primes(numbers)
print("Prime Numbers:", prime_numbers)

# 3. Set Operations
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
intersection, union, difference_a, difference_b = set_operations(list_a, list_b)
print("Set Intersection:", intersection)
print("Set Union:", union)
print("A - B:", difference_a)
print("B - A:", difference_b)

# 4. Compose Song
notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2
song = compose(notes, moves, start_position)
print("Composed Song:", song)

# 5. Replace Below Main Diagonal
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
modified_matrix = replace_below_diagonal(matrix)
print("Modified Matrix:")
for row in modified_matrix:
    print(row)

# 6. Find Items Occurring x Times
list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
x = 2
items_x_times = find_x_times_in_lists(x, list1, list2, list3, list4)
print(f"Items occurring {x} times:", items_x_times)

# 7. Palindrome Count and Max
numbers = [121, 123, 1331, 55, 777]
count, max_palindrome = find_palindromes(numbers)
print(f"Number of Palindromes: {count}")
print(f"Max Palindrome: {max_palindrome}")

# 8. ASCII Divisibility
strings = ["test", "hello", "lab002"]
x_value = 2
flag_value = False
result = ascii_divisibility(strings, x_value, flag_value)
print("ASCII Divisibility Result:", result)

# 9. Spectator Seats
stadium = [[1, 2, 3, 2, 1, 1],
           [2, 4, 4, 3, 7, 2],
           [5, 5, 2, 5, 6, 4],
           [6, 6, 7, 6, 7, 5]]
obstructed_seats = find_obstructed_seats(stadium)
print("Obstructed Seats:", obstructed_seats)

# 10. Group Lists
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]
grouped_lists = group_lists(list1, list2, list3)
print("Grouped Lists:")
for group in grouped_lists:
    print(group)

# 11. Sort Tuple List
tuples = [('abc', 'bcd'), ('abc', 'zza')]
sorted_tuples = sort_tuple_list(tuples)
print("Sorted Tuple List:", sorted_tuples)

# 12. Group by Rhyme
words = ['ana', 'banana', 'carte', 'arme', 'parte']
rhyme_groups = group_by_rhyme(words)
print("Rhyme Groups:", rhyme_groups)
