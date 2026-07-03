arr = [10, 30, 20, 40, 50]

is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False

if is_sorted:
    print("array is sorted")
else:
    print("array is not sorted")
