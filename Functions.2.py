# 2. Compute n + nn + nnn + nnnn
def compute(n):
    n = str(n)
    return int(n) + int(n*2) + int(n*3) + int(n*4)

print("2:")
for i in range(4, 8):
    print(f"n={i} -> {compute(i)}")
