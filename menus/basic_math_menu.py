from basic_math.long_addition import long_addition

def show_basic_math_menu():
    while True:
        print("\n=== Basic Math ===")
        print("1. Long Addition")
        print("0. Back")
        choice = input("Choose an option: ")

        match choice:
            case "1":
                    a = int(input("Enter first number: "))
                    b = int(input("Enter second number: "))
                    long_addition(a, b)
            case "0":
                break
            case _:
                print("Invalid input")
