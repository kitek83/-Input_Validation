import pyinputplus as pyip
response = pyip.inputNum('Enter the nr:')
print(response)
response = pyip.inputNum(blank=True)
print('---------')
print()

response = pyip.inputNum('Enter nr 2 times:', limit=2)

response = pyip.inputNum(timeout=5)

