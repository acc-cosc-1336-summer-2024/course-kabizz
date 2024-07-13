import dictionary  

def is_valid_dna_string(dna_string):
    """
    Check if a given string consists only of 'A', 'T', 'G', 'C' characters.
    """
    valid_bases = set('ATGC')
    return all(base in valid_bases for base in dna_string)

def main():
    while True:
        print("1- Get p-distance matrix")
        print("2- Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            dna_strings = []
            while True:
                try:
                    n = int(input("Enter number of DNA strings: "))
                    break  # Break out of the loop if input is a valid integer
                except ValueError:
                    print("Invalid input. Please enter a number.")

            for i in range(n):
                while True:
                    dna_string = input(f"Enter DNA string {i+1}: ").strip().upper()
                    if is_valid_dna_string(dna_string):
                        dna_strings.append(list(dna_string))
                        break
                    else:
                        print("Invalid DNA string. Please enter only 'A', 'T', 'G', 'C' characters.")

            try:
                distance_matrix = dictionary.get_p_distance_matrix(dna_strings)

                print("p-distance matrix:")
                for row in distance_matrix:
                    print(' '.join(f'{dist:.5f}' for dist in row))
            
            except AttributeError:
                print("Error: 'dictionary' module does not have 'get_p_distance_matrix' function.")
        
        elif choice == '2':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

