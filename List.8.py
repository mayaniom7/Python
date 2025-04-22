queue = []

while True:
    print("\nQueue Menu")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display Queue")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        element = input("Enter the element to enqueue: ")
        queue.append(element)
        print(f"Element '{element}' enqueued.")
    elif choice == 2:
        if queue:
            dequeued_element = queue.pop(0)
            print(f"Element '{dequeued_element}' dequeued.")
        else:
            print("Queue is empty.")
    elif choice == 3:
        print("Current Queue:", queue)
    elif choice == 4:
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")
