import re

def validate_password(password):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_+=])[A-Za-z\d!@#$%^&*()-_+=]{8,}$"
    return bool(re.match(regex, password))

def validate_password2(password1,password2):
    return password1==password2

def validate_username(username):
    regex = r'^[a-zA-Z]+$'
    return bool(re.match(regex, username))

def validate_email(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(regex, email))



def checkBirthDay():
    return False

