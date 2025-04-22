# 6. List of (x, x^2, x^3)
def tuple_list(n):
    return [(x, x**2, x**3) for x in range(1, n+1)]

print("6:", tuple_list(5))
