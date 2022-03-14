import pyinputplus as pyip
import random,time

numberOfQuestions = 10
correctAnswers = 0
for qustionNumber in range(numberOfQuestions):
    num1 = random.randint(0,9)
    num2= random.randint(0,9)
    prompt = '#%s: %sx%s, enter result: ' % (qustionNumber+1,num1,num2)
    #print(prompt) #for checking
    try:
        pyip.inputStr(prompt,allowRegexes=['^%s$'% (num1*num2)], blockRegexes=[('*.','Incorrect!')],timeout=5,limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else: #this block runs if not exceptions were rised in the try block
        correctAnswers += 1
    print('Great!Correct answer!')
    time.sleep(1)

print('correct answers: %s/number of questions: %s' % (correctAnswers,numberOfQuestions))

