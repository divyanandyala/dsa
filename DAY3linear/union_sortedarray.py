# arr1 = [1, 1, 2, 3, 4]
# arr2 = [2, 3, 4, 4, 5]

# result = []

# for num in arr1:
#     if num not in result:
#         result.append(num)

# for num in arr2:
#     if num not in result:
#         result.append(num)

# result.sort()

# print("Union:", result)



arr1 = [1, 1, 2, 3, 4]
arr2 = [2, 3, 4, 4, 5]

result = set()

for num in arr1:
    result.add(num)

for num in arr2:
    result.add(num)

answer = sorted(result)

print("Union:", answer)