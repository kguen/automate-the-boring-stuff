import random, time, pyinputplus as pyip

numberOfQuestions = 10
correctAnswer = 0

for questionIdx in range(numberOfQuestions):
    firstArg = random.randint(0, 9)
    secondArg = random.randint(0, 9)
    try:
        response = pyip.inputInt(
            f'#{questionIdx + 1}: {firstArg} x {secondArg} = ',
            blockRegexes=[(r'.*', 'Incorrect!')], # Block all other values
            allowRegexes=[rf'^{firstArg * secondArg}$'], # except firstArg * secondArg
            timeout=8, 
            limit=3
        )
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correctAnswer += 1
    
    # Pause 1 second for user to see response prompt
    time.sleep(1)

print(f'Your score: {correctAnswer}/{numberOfQuestions}')