arr = [10, 0, 20, 0, 30]

new_arr = []
count = 0

for num in arr:
    if num != 0:
        new_arr.append(num)
    else:
      count = count + 1

for i in range(count):
    new_arr.append(0) 

print(new_arr)                

