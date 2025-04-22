random_numbers = [random.randint(1, 100) for _ in range(20)]
print("Random Numbers:", random_numbers)

user_number = int(input("Enter a number to find its positions: "))

positions = [index for index, num in enumerate(random_numbers) if num == user_number]

if positions:
    print(f"The number {user_number} occurs at positions: {positions}")
else:
    print(f"The number {user_number} is not present in the list.")
