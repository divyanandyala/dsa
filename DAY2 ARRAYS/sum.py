arr=list(map(int,input("enter a list").split()))
total=0
for i in range(len(arr)):
    total=arr[i]+total
    print(total)
print(total)