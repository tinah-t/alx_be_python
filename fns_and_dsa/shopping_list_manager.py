def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice.isnumeric():
            if choice == '1':
                # Prompt for and add an item
                item = input("Enter the item to add: ")
                if item.isnumeric():
                    shopping_list.append(item)
                else:
                    print("Input must be a number")
                pass
            elif choice == '2':
                item = input("Enter the item to remove: ")
                if ((item in shopping_list) and item.isnumeric()) :
                    shopping_list.remove(item)
                else:
                    print("Try again")
                pass
            elif choice == '3':
                print(shopping_list)
                pass
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            print("The choice must be a number")

if __name__ == "__main__":
    main()