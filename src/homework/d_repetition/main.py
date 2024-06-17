import repetition

while True:
    try:
        num = int(input('1. Enter a number between 1 and 10 to get its factorial: '))
        average = repetition.get_factorial(num)
        if num < 1 or num > 10:
            raise ValueError
        print(average)
        break
    except ValueError:
        print('Wrong Entry.')

