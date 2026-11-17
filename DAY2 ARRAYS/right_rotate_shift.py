#brute force

# arr=[1,2,3,4,5,6,7,8,9,10] # 6, 7, 8, 9, 10, 1, 2, 3, 4, 5
# d=5
# n=len(arr)
# for i in range(d):
#     last=arr[n-1]
#     for j in range(n-1,0,-1):
#         arr[j]=arr[j-1]
#     arr[0]=last
# print(arr)


#better

# arr=[1,2,3,4,5,6,7,8,9,10] # 6, 7, 8, 9, 10, 1, 2, 3, 4, 5
# d=5
# n=len(arr)
# d=d%n
# temp=[]
# for i in range(n-d,n):
#     temp.append(arr[i])
# for j in range(n-d-1,-1,-1):
#         arr[j+d]=arr[j]
# for i in range(d):
#     arr[i]=temp[i]
# print(arr)


# optimal
def reverse(arr, start, end):

    while start < end:

        arr[start], arr[end] = arr[end], arr[start]

        start += 1
        end -= 1


arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

n = len(arr)
k = k % n

reverse(arr, 0, n-1)

reverse(arr, 0, k-1)

reverse(arr, k, n-1)

print(arr)
