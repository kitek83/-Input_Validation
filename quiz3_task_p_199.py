import pyinputplus as pyip
import random
nrOfQuestions = 10
correctAnswers = 0
for question in range(nrOfQuestions):
    try:
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)
        prompt = '%s:%sx%s=' % (question +1,num1,num2)

        answer = pyip.inputStr(prompt,allowRegexes=['^%s$'% (num1*num2)],blockRegexes=[('*.','incorrect input')],timeout=8,limit=3)
        if answer:
            print('Correct answer!')
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of limits!')
    else:
        correctAnswers += 1
print('Correct answers: %s / number of questions: %s' % (correctAnswers,nrOfQuestions))

