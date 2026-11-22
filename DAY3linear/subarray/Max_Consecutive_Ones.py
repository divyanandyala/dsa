# arr=[1,1,0,0,0,1,1,1,1,0]
# n=len(arr)
# maxi=0
# for i in range(n):
#     count=0
#     for j in range(i,n):
#         print(i,j)
#         if arr[j]==1:
#             count+=1
#             maxi=max(maxi,count)
#             # print(maxi)
#         else:
#             count=0
#             break
# print(maxi)



# better

# arr=[1,1,0,0,1,1,0]
# maxi=0
# count=0
# for i in range(len(arr)):
#     if arr[i]==1:
#         count+=1
#         maxi=max(maxi,count)
#     else:
#         count=0
# print(maxi)


# optimal

arr=[1,1,1,0,0]
current=0
longest=0
for num in arr:
    if num==1:
        current+=1
    else:
        current=0
    if current>longest:
        longest=current
print(longest)