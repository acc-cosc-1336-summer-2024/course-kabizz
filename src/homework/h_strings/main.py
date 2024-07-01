import strings

def menu():
    while True:
        print("Menu:")
        print("1. Hamming Distance")
        print("2. DNA Complement")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("You selected Option 1")
            while True:
                try:
                    seq1 = input('Enter a DNA Sequence: ')
                    seq2 = input('Enter a second DNA Sequence of equal length: ')
                    if len(seq1) != len(seq2):
                        raise ValueError
                    distance = strings.get_hamming_distance(seq1, seq2)
                    print(f"Hamming distance between '{seq1}' and '{seq2}' is {distance}")
                    break
                except ValueError:
                    print("Must be same length")
                

            while True:
                choice = input("Enter '1' to return to main menu or '2' to Exit: ")
                if choice == '1':
                    break
                elif choice == '2':
                    print("Exiting...")
                    return
                else:
                    print("Invalid choice. Please select again.")
        
        elif choice == '2':
            print("You selected Option 2")
            while True:
                try:
                    dna_sequence = "ATCG"
                    complementary_sequence = strings.complement_sequence(dna_sequence)
                    print(f"Original sequence: {dna_sequence}")
                    print(f"Complementary sequence: {complementary_sequence}")
                    break
                except ValueError:
                    print('Wrong Entry. Please enter a number between 1 and 100.')
            while True:
                choice = input("Enter '1' to return to main menu or '2' to Exit: ")
                if choice == '1':
                    break
                elif choice == '2':
                    print("Exiting...")
                    return
                else:
                    print("Invalid choice. Please select again.")
                    
        elif choice == '3':  # choice 3 exits the program
            while True:
                try:
                    print("Enter yes if you want to exit")
                    print("Enter no if you want to return to the main menu")
                    exit_choice = input("Choose your answer: ")
                    if exit_choice.lower() == 'yes':
                       print("Exiting...")
                       exit()
                    elif exit_choice.lower() == 'no':
                       break
                    else:
                       print("Invalid choice, please enter 'yes' or 'no'.")
                except Exception as e:
                    print(f"An error occurred: {e}")
menu()



