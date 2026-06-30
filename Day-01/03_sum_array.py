def find_sum(arr):
    total = 0

    for num in arr:
        total = total + num

    return total


arr = [5, 6, 7, 8]
print(find_sum(arr))