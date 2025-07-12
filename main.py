from menus.basic_math_menu import show_basic_math_menu

def main():
    while True:
        print("\n=== Math CLI ===")
        print("1. Basic Math")
        print("2. Algebra (coming soon)")
        print("3. Calculus (coming soon)")
        print("0. Exit")

        choice = input("Choose an option: ")

        match choice:
            case "1":
                show_basic_math_menu()
            case "0":
                print("Stopping SimpleMathCLI")
                break
            case _:
                print("Invalid input")

if __name__ == "__main__":
    main()
