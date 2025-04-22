# 3. Create a 3D array
def create_array(x, y, z, value):
    return [[[value for _ in range(z)] for _ in range(y)] for _ in range(x)]

print("3:", create_array(2, 2, 2, 9))
