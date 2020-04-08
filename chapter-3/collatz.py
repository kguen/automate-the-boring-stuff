def collatz(number):
    if number % 2 == 0:
        newNum = int(number / 2)
    else:
        newNum = number * 3 + 1
    print(newNum)
    return newNum

while (True):
    print("Enter a number: ", end="")
    try:
        number = int(input())
        break
    except ValueError:
        print("Not a number!")

while (True):
    number = collatz(number)
    if number == 1:
        break