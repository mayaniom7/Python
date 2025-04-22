import random

odd_integers = [random.choice(range(1, 100, 2)) for _ in range(5)]
even_integers = [random.choice(range(2, 101, 2)) for _ in range(4)]

print("Original Odd Integers:", odd_integers)
print("Even Integers:", even_integers)

odd_integers[2] = even_integers
print("Odd Integers after replacing third element:", odd_integers)

flattened_list = [item for sublist in odd_integers for item in (sublist if isinstance(sublist, list) else [sublist])]
flattened_list.sort()

print("Flattened and Sorted List:", flattened_list)
