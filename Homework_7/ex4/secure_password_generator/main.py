from generator import generate_password

password_length = 16
include_special_characters = True
include_numbers = True
include_mixed_case = True

password = generate_password(
    length=password_length,
    include_special=include_special_characters,
    include_numbers=include_numbers,
    include_mixed_case=include_mixed_case
)

print(f"Generated Password: {password}")
