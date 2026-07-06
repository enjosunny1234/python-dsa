arr1 = [10, 20, 30, 40]
arr2 = [30, 40, 50]

new_arr = []

for num in arr1:
    if num not in new_arr:
        new_arr.append(num)

for num in arr2:
    if num not in new_arr:
        new_arr.append(num)

print(new_arr)
