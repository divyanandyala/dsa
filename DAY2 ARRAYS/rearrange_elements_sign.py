# # brute force

# arr=[1,-2,3,-4,5,-6]
# n=len(arr)
# pos=[]
# neg=[]
# for num in arr:
#     if num>0:
#         pos.append(num)
#     else:
#         neg.append(num)
# result=[]
# for i in range(n//2):
#     result.append(pos[i])
#     result.append(neg[i])
# print(result)


# better


arr=[1,-2,3,-4,5,-6]
n=len(arr)
pos=0
neg=1
result=[0]*n
for num in arr:
    if num>0:
        result[pos]=num
        pos+=2
    else:
        result[neg]=num
        neg+=2
print(result)
