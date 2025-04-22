import random

random_numbers = set(random.sample(range(15, 46), 10))
print("Original Set:", random_numbers)

count_less_than_30 = sum(1 for num in random_numbers if num < 30)
print("Count of numbers less than 30:", count_less_than_30)

# Remove numbers greater than 35
filtered_numbers = {num for num in random_numbers if num <= 35}
print("Filtered Set (<= 35):", filtered_numbers)
