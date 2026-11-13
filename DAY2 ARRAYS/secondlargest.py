arr=list(map(int,input("enter a values").split()))
largest=arr[0]
second=None
for i in range(len(arr)):
    if arr[i]>largest:
        second=largest
        largest=arr[i]
    elif arr[i]!=largest and(second is None or arr[i]>second):
        second=arr[i]
print(second)