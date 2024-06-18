def get_factorial(num):
    fact = 1
    for num in range(1, num + 1):
        fact *= num
    return fact
 
def sum_odd_numbers(num):
    sum = 0
    i = 1  
    while i <= num:
        sum += i
        i += 2  
    return sum

