arr = [ 10, 0, 5, 20, 0, 5]
count = 0

for num in arr:
    if num == 0:
        count = count + 1

print("total zeros=", count)