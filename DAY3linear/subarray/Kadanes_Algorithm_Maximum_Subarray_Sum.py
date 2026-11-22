# arr=[-2,1,-3,4,-1,2,1,-5,4]
# n=len(arr)
# maxi=float('-inf')
# for i in range(n):
#     for j in range(i,n):
#         total=0
#         for k in range(i,j+1):
#             total+=arr[k]
#         maxi=max(maxi,total)
# print(maxi)



# better

# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# n = len(arr)
# maximum = float('-inf')

# for i in range(n):

#     total = 0

#     for j in range(i, n):

#         total += arr[j]

#         maximum = max(maximum, total)

# print("Maximum subarray sum:", maximum)


# optimal

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
maximum = arr[0]

for i in range(1, len(arr)):

    current_sum = max(arr[i], current_sum + arr[i])

    maximum = max(maximum, current_sum)

print("Maximum subarray sum:", maximum)