arr = [4, 1, 5, 2, 4, 1, 2]

counts = {}

for num in arr:
    counts[num] = counts.get(num, 0) + 1

index = -1
for i in range(len(arr)):
    if counts[arr[i]] == 1:
        index = i
        break

print(index)
