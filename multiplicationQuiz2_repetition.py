import pyinputplus as pyip
import time, random
wins = 0
numberOfDraws = 10

for draw in range(numberOfDraws):
    try:

            num1 = random.randint(0,9)
            num2 = random.randint(0,9)
            prompt = '#%s: %sx%s result=' % (draw+1,num1,num2)

            pyip.inputStr(prompt, allowRegexes=['^%s$'%(num1*num2)],blockRegexes=['*.', 'Incorrect!'],timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of time.')
    except pyip.RetryLimitException:
        print('Out of tries.')

    else:
        wins += 1

    time.sleep(1)
    # displaing the result
print('correct answers:%s/ number of questions:%s' % (wins,draw+1))
