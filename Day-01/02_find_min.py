def find_min(arr):
    minimum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num

    return minimum


arr = [5, 6, 7, 8]
print(find_min(arr))
