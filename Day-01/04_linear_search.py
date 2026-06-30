def linear_search(arr, target):
    for num in arr:
        if num == target:
            return num

    return None


arr = [5, 6, 7, 8]
target = 7

print(linear_search(arr, target))