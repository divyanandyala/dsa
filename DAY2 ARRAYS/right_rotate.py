# def right_rotate_brute(arr):
#     n = len(arr)
#     temp = [0] * n

#     temp[0] = arr[n-1]

#     for i in range(n-1):
#         temp[i+1] = arr[i]

#     return temp

# print(right_rotate_brute([1, 2, 3, 4, 5]))



# def right_rotate_better(arr):
#     if len(arr) <= 1:
#         return arr

#     return [arr[-1]] + arr[:-1]

# print(right_rotate_better([1, 2, 3, 4, 5]))



def right_rotate_optimal(arr):
    n = len(arr)

    if n <= 1:
        return arr

    temp = arr[n-1]

    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]

    arr[0] = temp

    return arr

print(right_rotate_optimal([1, 2, 3, 4, 5]))




