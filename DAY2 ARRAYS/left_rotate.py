def left_brute_force(arr):
    n=len(arr)
    temp=[0]*n
    for i in range(1,n):
        temp[i-1]=arr[i]
    temp[n-1]=arr[0]
    return temp

print(left_brute_force([1,2,3,4,5]))