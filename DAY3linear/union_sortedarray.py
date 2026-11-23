arr1 = [1, 1, 2, 3, 4]
arr2 = [2, 3, 4, 4, 5]

result = []

for num in arr1:
    if num not in result:
        result.append(num)

for num in arr2:
    if num not in result:
        result.append(num)

result.sort()

print("Union:", result)