arr = [2, 3, 5, 4, 5, 3, 2]

n = len(arr)

for i in range(n):

    count = 0

    for j in range(n):

        if arr[i] == arr[j]:
            count += 1

    if count == 1:
        print("Number appears once:", arr[i])
        break
    