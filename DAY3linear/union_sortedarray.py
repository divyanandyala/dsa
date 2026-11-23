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



# arr1 = [1, 1, 2, 3, 4]
# arr2 = [2, 3, 4, 4, 5]

# result = set()

# for num in arr1:
#     result.add(num)

# for num in arr2:
#     result.add(num)

# answer = sorted(result)

# print("Union:", answer)



arr1 = [1, 1, 2, 3, 4]
arr2 = [2, 3, 4, 4, 5]

n = len(arr1)
m = len(arr2)

i = 0
j = 0

result = []

while i < n and j < m:

    if arr1[i] <= arr2[j]:

        if len(result) == 0 or result[-1] != arr1[i]:
            result.append(arr1[i])

        i += 1

    else:

        if len(result) == 0 or result[-1] != arr2[j]:
            result.append(arr2[j])

        j += 1

while i < n:

    if len(result) == 0 or result[-1] != arr1[i]:
        result.append(arr1[i])

    i += 1

while j < m:

    if len(result) == 0 or result[-1] != arr2[j]:
        result.append(arr2[j])

    j += 1

print("Union:", result)