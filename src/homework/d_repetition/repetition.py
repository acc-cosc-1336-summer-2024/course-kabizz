def get_factorial(num):
    fact = 1
    for num in range(1, num + 1):
        fact *= num
    return fact
 
def sum_odd_numbers(num1):
    value = 1
    total = 0
    while value < (2*num1) - 1:
        if value % 2 == 1:
            total += value
        value += 1
    return total

