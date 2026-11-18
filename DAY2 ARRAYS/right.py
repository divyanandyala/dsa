arr=[1,2,3,4,5]
n=len(arr)
d=2
d=d%n
temp=[]
for i in range(n,n-d,-1):
    temp.append(arr[i])
for i in range(d):
    temp.append(arr[i])
print(temp)