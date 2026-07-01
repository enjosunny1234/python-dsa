arr = [45, 12, 78, 3, 90]

smallest = arr[0]

for num in arr:
    if num < smallest:
        smallest = num

print("Smallest =", smallest)