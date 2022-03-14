import pyinputplus as pyip
#creatring custom validation
def addToTen(numbers):
    listNumebers = list(numbers)
    print(listNumebers)
    #convertin string listNumbers to int listNUmbers
    for index,digit in enumerate(listNumebers):
        listNumebers[index] = int(digit)
        print(listNumebers)
    if sum(listNumebers) != 10:
        print('The digits must add up to 10, not to: %s.'% sum(listNumebers))
    else:
        print('This is right number. Sum of numers= %d'% sum(listNumebers))


print('Enter the number. Digits of the number will be added to each other: ',end='')
response = pyip.inputCustom(addToTen)