import pyinputplus as pyip

def appUpToTen(numbers):
    numbersList = list(numbers)
    print(numbersList)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
        print(numbersList)
    print(numbersList)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.'% sum(numbersList))
    return int(numbers)

print('Enter the number:',end='')
response1 =  pyip.inputCustom(appUpToTen)