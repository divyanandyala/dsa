
#bruteforce

# arr=[1,2,3,4,5,6,7]
# d=3
# n=len(arr)
# temp=[]
# for i in range(d):
#     temp.append(arr[i])
# print(temp)
# for i in range(d,n):
#     arr[i-d]=arr[i]
# for i in range(d):
#     arr[n-d+i] = temp[i]

# print(arr)


#better
# arr = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12]
# d = 9

# n = len(arr)
# d = d % n

# temp = []


# for i in range(d):
#     temp.append(arr[i])


# for i in range(d, n):
#     arr[i-d] = arr[i]


# for i in range(d):
#     arr[n-d+i] = temp[i]

# print(arr)


#better
arr=[1,2,3,4,5,6,7,8,9,10]
n=len(arr)
d=2
d=d%n
temp=[]
for i in range(d,n):
    temp.append(arr[i])
for i in range(d):
    temp.append(arr[i])
print(temp)

#optimal

def reverse(arr, start, end):

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]

        start += 1
        end -= 1


arr = [1, 2, 3, 4, 5, 6, 7]
d = 3

n = len(arr)
d = d % n

reverse(arr, 0, d-1)

reverse(arr, d, n-1)

reverse(arr, 0, n-1)

print(arr)