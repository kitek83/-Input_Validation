import pyinputplus as pyip
def addToTen(numbers):
    listNumbers = list(numbers)
    print(listNumbers)
    for i,digit in enumerate(listNumbers):
        listNumbers[i] = int(digit)
        print(listNumbers)
    if sum(listNumbers) != 10:
        raise Exception('Digits must add up to 10, not to %s.' % sum(listNumbers)) #looks like function sum() returns string?

print('Enter the number: ',end='')
response = pyip.inputCustom(addToTen)