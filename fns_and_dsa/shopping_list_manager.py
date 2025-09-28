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

        if choice == '1':
            # Prompt for and add an item
            item = input("What number do you want to add to the list?")
            shopping_list.append(item)
            pass
        elif choice == '2':
            item = input("What number do you want to remove from the list?")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item is not found")
            pass
        elif choice == '3':
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()