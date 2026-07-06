arr = [2, 3, 5, 3, 2]

new_arr = []

for num in arr:
    if num not in new_arr:
       new_arr.append(num) 

print(new_arr)        
