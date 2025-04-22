# 4. Sum and average of marks
def sum_avg(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg

print("4:", sum_avg([88, 76, 90, 85, 69]))
