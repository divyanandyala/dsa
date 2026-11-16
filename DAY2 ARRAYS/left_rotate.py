# def left_brute_force(arr):
#     n=len(arr)
#     temp=[0]*n
#     for i in range(1,n):
#         temp[i-1]=arr[i]
#     temp[n-1]=arr[0]
#     return temp

# print(left_brute_force([1,2,3,4,5]))




# def left_rotate_better(arr):
#     if len(arr) <= 1:
#         return arr

#     return arr[1:] + [arr[0]]

# print(left_rotate_better([1, 2, 3, 4, 5]))


def left_rotate_optimal(arr):
    n = len(arr)
    if n <= 1:
        return arr

    temp = arr[0]  #=1

    #  SHIFT:  1,2,3,4
    for i in range(1, n):
        arr[i-1] = arr[i]
        print(f"After i={i}, arr = {arr}, temp = {temp}")

    arr[n-1] = temp  
    return arr

print(left_rotate_optimal([1,2,3,4,5]))
