import pyinputplus as pyip
respond = pyip.inputNum('Enter sth:',allowRegexes=[r'I|V|X|L|C|D|M', r'zero']),
print(respond)

stationary = ['notebooks','staplers','pens','pencils']
for index, item in enumerate(stationary):
    print('Index:' + str(index) + ' item: ' +item)