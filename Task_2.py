import string
import random

def generate_password():
    # Prompt user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 6): "))
            if length < 6:
                print("Password length should be at least 6 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Define character pools for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character pools
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure the password contains at least one character from each pool
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length of the password with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

if __name__ == "__main__":
    print("Generated Password:", generate_password())
