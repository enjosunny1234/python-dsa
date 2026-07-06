arr = [10, 20, 10, 30, 10, 40, 20]
target = 10

count = 0

for num in arr:
    if num == target:
        count = count + 1

print("frequency of number is =", count)