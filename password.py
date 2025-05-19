import random

def user(length, special, digitgs, upper, lower):
    
    password = ""
    for i in range(length):
        # Generate a random character from the ASCII character set
        # (33 to 126)
        password += chr(random.randint(33, 126))
    return password


user(int(input("Enter the length of the password: ")), input("Do you want special characters? (y/n): "), input("Do you want digits? (y/n): "), input("Do you want uppercase letters? (y/n): "), input("Do you want lowercase letters? (y/n): "))
    
