arr = [1, 2, 3, 2, 1]

is_palindrome = True

for i in range(len(arr) // 2):
    if arr[i] != arr[len(arr) - 1 - i]:
        is_palindrome = False
    
if is_palindrome:
     print("The array is a palindrome")
else:
    print("The array is not a palindrome")
