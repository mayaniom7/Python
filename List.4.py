random_numbers = [random.randint(-50, 50) for _ in range(30)]
print("Generated Random Numbers:", random_numbers)

positive_numbers = [num for num in random_numbers if num > 0]
negative_numbers = [num for num in random_numbers if num < 0]

print("Positive Numbers:", positive_numbers)
print("Negative Numbers:", negative_numbers)
