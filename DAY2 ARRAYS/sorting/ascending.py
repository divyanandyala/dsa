
arr = [5, 2, 8, 1, 3]

n = len(arr)

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Ascending:", arr)
