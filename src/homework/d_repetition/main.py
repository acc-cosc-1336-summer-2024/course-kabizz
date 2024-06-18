import repetition

def menu():
    while True:
        #menu fo the end user
        print("Menu:")
        print("1. Find a Factorial number between 1 and 10")
        print("2. Find sum of odd numbers between 1 and 100")
        print("3. Exit")
        #Prompt for end user to enter a choice on the menu
        choice = input("Enter your choice: ")
        
        if choice == '1':#Choice 1 gives you factorial program
            print("You selected Option 1")
            while True:
                try:
                    num = int(input('1. Enter a number between 1 and 10 to find its factorial: '))
                    average = repetition.get_factorial(num)#Calls get_factorial function 
                    if num < 1 or num > 10:#Validates the number is between 1 and 10
                     raise ValueError
                    print(average)
                    break
                except ValueError:
                    print('Wrong Entry. Please enter a number between 1 and 10.')
        
        elif choice == '2':#Choice 2 gives you sum of the odd numbers program
            print("You selected Option 2")
            while True:
                try:
                    num = int(input('Enter a number between 1 and 100 to find the sum of all odd numbers up to that number: '))
                    answer = repetition.sum_odd_numbers(num)#Calls sum_odd_number function
                    if num < 1 or num > 100:#Validates the number is between 1 and 100
                        raise ValueError
                    print(answer)
                    break
                except ValueError:
                    print('Wrong Entry. Please enter a number between 1 and 100.')
        
        elif choice == '3': #choice 3 exits the program
            print("Exiting the program. Goodbye!")
            break
        
        else:
             #Prompts user to pick a choice in the menu if the wrong number is picked
            print("Invalid choice. Please enter a number between 1 and 3.")
menu()