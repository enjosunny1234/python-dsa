arr = [50, 20, 80, 10, 40]

smallest = arr[0]
second = arr[0]

for num in arr:
    if num < smallest:
        second = smallest
        smallest = num
    elif num < second and num > smallest:
        second = num

print("second smallest =", second)   