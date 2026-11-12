# arr=list(map(int,input("enter a values").split()))
# count=0
# for i in range(len(arr)):
#     if arr[i]%2==0:
#         count=count+1
# print(count)


# odd


arr=list(map(int,input("enter a values").split()))
count=0
for i in range(len(arr)):
    if arr[i]%2!=0:
        count=count+1
print(count)