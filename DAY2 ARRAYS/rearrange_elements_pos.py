# arr=[1,2,-3,-4,5,6]
# n=len(arr)
# pos=[]
# neg=[]
# for num in arr:
#     if num>0:
#         pos.append(num)
#     else:
#         neg.append(num)
# result=[]
# num=0
# while num<len(neg):
#     result.append(pos[num])
#     result.append(neg[num])
#     num+=1
# while num<len(pos):
#     result.append(pos[num])
#     num+=1
# print(result)



# better


# optimal
arr = [1, 2, -3, -4, 5, 6]

pos = []
neg = []

for num in arr:
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)

result = []

i = 0

while i < min(len(pos), len(neg)):
    result.append(pos[i])
    result.append(neg[i])
    i += 1

result.extend(pos[i:])
result.extend(neg[i:])

print(result)