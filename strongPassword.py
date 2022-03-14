#program shows, that passwor is strong if thre is at least 1 uppercase, 1 lowercase, 1 diggit and
# has 8 or more characters
import re
def upperCaseCheck(password):
    if re.search('[A-Z]', password):
        return True
    return False
def lowercaseCheck(password):
    if re.search('[a-z]',password):
        return True
    return False
def isDigit(password):
    if re.search('[0-9]',password):
        return True
    return False

password = input('Enter the passwor for checking: ')
if len(password) >= 8 and upperCaseCheck(password) and lowercaseCheck(password) and isDigit(password):
    print('Password is strong!')
else:
    print('Password is weak!')