def linear_search(arr, target):
    for num in arr:
        if num == target:
            return True

    return False


arr = [5, 6, 7, 8]

print(linear_search(arr, 7))
print(linear_search(arr, 10))