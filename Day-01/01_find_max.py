def find_max(arr):
    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num

    return maximum


arr = [5, 6, 7, 8]
print(find_max(arr))