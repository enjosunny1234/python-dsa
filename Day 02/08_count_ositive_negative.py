arr = [10, -5, 20, -8, 0, 15, -2]

positive = 0
negative = 0

for num in arr:
    if num > 0:
        positive = positive + 1
    elif num < 0:
        negative = negative + 1

print("Positive =", positive)
print("Negative =", negative)