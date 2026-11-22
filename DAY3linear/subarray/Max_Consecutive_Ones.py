arr=[1,1,0,0,0,1,1,1,1,0]
n=len(arr)
maxi=0
for i in range(n):
    count=0
    for j in range(i,n):
        print(i,j)
        if arr[j]==1:
            count+=1
            maxi=max(maxi,count)
            # print(maxi)
        else:
            count=0
            break
print(maxi)