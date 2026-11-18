arr=[1,0,2,0,3]
temp=[]
for i in arr:
    if i !=0:
        temp.append(i)
zeroes=len(arr)-len(temp)
for i in range(zeroes):
    temp.append(0)
print(temp)