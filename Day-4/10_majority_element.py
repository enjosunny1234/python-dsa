arr = [ 1, 2, 3, 1, 3, 2]

count = 0

for num in arr:
    if count ==0:
        candidate = num
        count = 1
    elif num == candidate:
        count = count = 1
    else:
        count = count - 1

check_count = 1
for num in arr:
    if num == candidate:
        check_count = check_count + 1

if check_count > len(arr) //2:
    print("majority element =", candidate)
else:
    print("no majority element found")                    