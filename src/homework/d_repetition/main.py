import repetition

def menu():
    while True:
        print("Menu:")
        print("1. Find a Factorial number between 1 and 10")
        print("2. Find sum of odd numbers between 1 and 100")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("You selected Option 1")
            while True:
                try:
                    num = int(input('1. Enter a number between 1 and 10 to find its factorial: '))
                    average = repetition.get_factorial(num)
                    if num < 1 or num > 10:
                     raise ValueError
                    print(average)
                    break
                except ValueError:
                    print('Wrong Entry. Please enter a number between 1 and 10.')
        
        elif choice == '2':
            print("You selected Option 2")
            while True:
                try:
                    num = int(input('Enter a number between 1 and 100 to find the sum of all odd numbers up to that number: '))
                    answer = repetition.sum_odd_numbers(num)
                    if num < 1 or num > 100:
                        raise ValueError
                    print(answer)
                    break
                except ValueError:
                    print('Wrong Entry. Please enter a number between 1 and 100.')
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 3.") 
menu()