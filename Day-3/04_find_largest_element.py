arr = [15, 42, 8, 90, 31]
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("largest element =", largest)