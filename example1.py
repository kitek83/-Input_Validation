while True:
    age = input('Enter Your age:')
    try:
        age = int(age)
    except:
        print('Please use numeric digits')
        continue
    if age < 1:
        print('Please enter a positive number: ')
        continue
    break