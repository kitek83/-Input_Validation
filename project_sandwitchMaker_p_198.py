#Program asks user for the sandwich preferences.
#Program uses pyinputplus to ensure valid input
import pyinputplus as pyip

print('What kind of bread wpuld you like?')
bread = pyip.inputMenu(['wheat','white','sourdough'])
print('What kind of protein would You like?')
protein = pyip.inputMenu(['chicken','turkey','ham','tofu'])

prompt = 'Wuould You like a cheese? Asnwer yes or no'
cheese = pyip.inputYesNo(prompt)
if cheese == 'yes':
    print('What kind of cheese would You like:')
    cheese = pyip.inputMenu(['cheddar','Swiss','mozzarella'])

print(pyip.inputInt('How many sandwitches do You want?',min=1))

