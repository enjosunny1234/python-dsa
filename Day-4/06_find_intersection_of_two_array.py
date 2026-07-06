arr1 = [10, 20, 30, 40]
arr2 = [30,40,50,60]

result = []

for num in arr1:
    if num in arr2:
        result.append(num)

print(result)        