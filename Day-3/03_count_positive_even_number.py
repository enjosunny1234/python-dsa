arr = [10, -4, 7, 8, -2, 15, 20]
count = 0

for num in arr:
    if num % 2 == 0 and num > 0:
        count = count + 1

print("total positive even numbers =", count)