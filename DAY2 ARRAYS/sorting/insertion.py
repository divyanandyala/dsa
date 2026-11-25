
# arr = [5, 3, 8, 2, 1]

# n = len(arr)

# for i in range(1, n):

#     key = arr[i]

#     j = i - 1

#     while j >= 0 and arr[j] > key:

#         arr[j + 1] = arr[j]

#         j -= 1

#     arr[j + 1] = key

# print("Sorted array:", arr)





arr = [1, 2, 3, 4, 5]

n = len(arr)

for i in range(1, n):

    if arr[i] >= arr[i - 1]:
        continue

    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)