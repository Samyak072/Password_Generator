import random
import string
import pyperclip  # This library allows copying text to the clipboard

def generate_password(length, chars):
    password = "".join(random.choice(chars) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length, chars):
    passwords = [generate_password(length, chars) for _ in range(num_passwords)]
    return passwords

def main():
    chars = string.ascii_letters + string.digits + string.punctuation
    length = 0
    while length <= 0:
        try:
            length = int(input("Enter Password Length (should be a positive integer): "))
            if length <= 0:
                print("Password length should be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

    password = generate_password(length, chars)
    print(f"Generated Password: {password}")

    regenerate = input("Do you want to regenerate? (y/n): ").lower()
    while regenerate == 'y':
        password = generate_password(length, chars)
        print(f"Generated Password: {password}")
        regenerate = input("Do you want to regenerate again? (y/n): ").lower()

    # Copy the password to the clipboard
    try:
        pyperclip.copy(password)
        print("Password copied to clipboard!")
    except pyperclip.PyperclipException:
        print("Failed to copy to clipboard. Please copy the password manually.")

    num_passwords = int(input("Enter the number of passwords to generate: "))
    if num_passwords > 1:
        passwords = generate_multiple_passwords(num_passwords, length, chars)
        print("\nGenerated Passwords:")
        for i, password in enumerate(passwords, 1):
            print(f"{i}. {password}")
        try:
            pyperclip.copy("\n".join(passwords))
            print("Passwords copied to clipboard!")
        except pyperclip.PyperclipException:
            print("Failed to copy passwords to clipboard. Please copy them manually.")

if __name__ == "__main__":
    main()
