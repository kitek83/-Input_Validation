import pyinputplus as pyip

response2 = pyip.inputNum('Enter nr again 2 times:',limit=2,default='N/A')
print(response2)

response3 = pyip.inputNum('Enter roman number: ',allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'])
print(response3)
print('-------------------')

response4 = pyip.inputNum('Enter the nr for blockReges: ', blockRegexes=[r'[012468]$'])
print(response4)