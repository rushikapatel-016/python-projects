import random
import string

def password_generator(length):
    characters = string.ascii_letters + string.digits
    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password

def random_name_picker(names):
    return random.choice(names)

def dice_roller():
    return random.randint(1, 6)