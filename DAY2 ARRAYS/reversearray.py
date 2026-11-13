arr=list(map(int,input("enter a values").split()))
rev=[]
for i in range(len(arr)-1,-1,-1):
    rev.append(arr[i])
print(rev)