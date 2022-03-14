import pyinputplus as pyip
question = 'Do you know how to keep an idiot busy for hours?'
while True:
    response = pyip.inputYesNo(question)
    if response == 'no':
        break
    print('Thank You!')