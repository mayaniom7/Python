stack = []

while True:
    print("\nStack Menu")
    print("1. Push")
    print("2. Pop")
    print("3. Display Stack")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        element = input("Enter the element to push: ")
        stack.append(element)
        print(f"Element '{element}' pushed to stack.")
    elif choice == 2:
        if stack:
            popped_element = stack.pop()
            print(f"Element '{popped_element}' popped from stack.")
        else:
            print("Stack is empty.")
    elif choice == 3:
        print("Current Stack:", stack)
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")
