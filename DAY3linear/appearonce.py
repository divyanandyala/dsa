# arr = [2, 3, 5, 4, 5, 3, 2]

# n = len(arr)

# for i in range(n):

#     count = 0

#     for j in range(n):

#         if arr[i] == arr[j]:
#             count += 1

#     if count == 1:
#         print("Number appears once:", arr[i])
#         break
    


arr = [2, 3, 5, 4, 5, 3, 2]

frequency = {}

for num in arr:

    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num in frequency:

    if frequency[num] == 1:
        print("Number appears once:", num)
        break