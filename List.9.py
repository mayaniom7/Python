list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]

third_list = [num for num in list1 if num not in list2]

print("Third List (elements from list1 not in list2):", third_list)
