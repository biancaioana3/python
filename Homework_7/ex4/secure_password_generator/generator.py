import random
import string


def generate_password(length=12, include_special=True, include_numbers=True, include_mixed_case=True):
    characters = string.ascii_letters
    if include_special:
        characters += string.punctuation
    if include_numbers:
        characters += string.digits

    if include_mixed_case:
        characters += string.ascii_uppercase

    password = ''.join(random.choice(characters) for _ in range(length))
    return password
