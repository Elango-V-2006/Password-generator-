import random
import string

def generate_password(length, include_digits=True, include_special_chars=True):
    """Generates a random password based on the specified criteria."""

    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        return "No character sets selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired password length: "))
        include_digits_input = input("Include digits? (yes/no): ").lower()
        include_special_chars_input = input("Include special characters? (yes/no): ").lower()

        include_digits = include_digits_input == 'yes'
        include_special_chars = include_special_chars_input == 'yes'

        password = generate_password(length, include_digits, include_special_chars)
        print("Generated Password:", password)

    except ValueError:
        print("Invalid input. Please enter a valid integer for length.")