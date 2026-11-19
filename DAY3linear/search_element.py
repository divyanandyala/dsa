# brute force

# arr=[10,20,30,40,50]
# target=80
# for i in range(len(arr)):
#     if arr[i]==target:
#         print("target found")
#         break
# else:
#     print("not found")


# better

# arr=[10,20,30,40]
# target=40
# for index,value in enumerate(arr):
#     if value==target:
#         print("element found")
#         break
# optimal
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1



arr=list(map(int,input("values").split()))
target=int(input())

result=linear_search(arr,target)
if result!=-1:
    print("element found")
else:
    print("not found")
