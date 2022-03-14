import pyinputplus as pyip
response1 = pyip.inputNum('Enter nr:', min=5)
print(response1)
response2 = pyip.inputNum('Enter nr:',greaterThan=5)
print(response2)
response3 = pyip.inputNum('Enter 3<num<6: ',min=3, lessThan=6)
print(response3)