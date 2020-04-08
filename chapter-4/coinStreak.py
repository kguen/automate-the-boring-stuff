import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    result = []
    for i in range(100):
        result.append(random.randint(0, 1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(0, 94):
        isStreak = True
        for j in range(0, 5):
            if result[i + j] != result[i + j + 1]:
                isStreak = False
                break
        if isStreak:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))