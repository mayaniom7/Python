random_numbers = [random.randint(1, 30) for _ in range(50)]
print("Original List:", random_numbers)

unique_numbers = list(set(random_numbers))
print("List with Duplicates Removed:", unique_numbers)
