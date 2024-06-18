def get_factorial(num):
    i = 1
    for num in range(1, num + 1):#The range(1, num + 1) generates a sequence of numbers starting at 1 and ending at num.
        i *= num #This is a shorthand for i = i * num. It effectively updates i to be the product of all numbers from 1 to num.
    return i
 
def sum_odd_numbers(num):
    sum = 0
    i = 1  
    while i <= num:#This line starts a while loop that continues to execute as long as i is less than or equal to num.
        sum += i #Updates sum to include the current odd number.
        i += 2  #This line increments i by 2. Since i is initially 1, adding 2 ensures that i will always be an odd number (1, 3, 5, 7, ...).
    return sum

