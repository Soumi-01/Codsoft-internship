import random
import string

def generate_password():
    # Prompt the user to specify the desired password length
    length = int(input("Enter the desired length for your password: "))
    
    # Define the characters to choose from (letters, digits, and punctuation)
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    # Display the generated password
    print(f"Generated Password: {password}")

# Call the generate_password function
generate_password()
