#this program shows a quiz. num1 is multiplied by num2 and user must enter right answer
import pyinputplus as pyip
import random, time
nrOfQuestions = 10
correctAnswers = 0
print('Write result of multiplication of 2 digits. You have 3 tries and time limit=8s for each answer.')
for question in range(nrOfQuestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    mult = num1 * num2
    prompt = '%s:%sx%s=' % (question + 1,num1,num2)
    try:
        answer = pyip.inputStr(prompt,allowRegexes=['^%s$'%(num1*num2)],blockRegexes=[('*,','Incorrects input')],timeout=8,limit=3)
        if answer:
            print('Correct answer')
        else:
            print('Wrongg answer! Try again!')
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        correctAnswers += 1

print('Corrects answers: %s / nr of questions: %s'% (correctAnswers,nrOfQuestions))