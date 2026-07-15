import string
import random

def generate_password(length: int, use_digits: bool, user_symbol: bool):

    strLower = string.ascii_lowercase
    strUpper = string.ascii_uppercase
    numberSTR = string.digits

    allString = strLower

    if use_digits:
        allString = allString + str(numberSTR)
    if user_symbol:
        allString = allString + strUpper

    password = ""

    for i in range(length):
        rand = random.randint(0, len(allString) - 1)

        password = password + allString[rand]
        
    print(len(password))
    print(password)
    
generate_password(10, True, True)