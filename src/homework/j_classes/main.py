import class_a

def main():
    die = class_a.Die()
    while True:
        die.roll()
        print(die)
        choice = input("Do you want to roll again? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()

