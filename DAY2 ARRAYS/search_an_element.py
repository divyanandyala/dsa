arr=list(map(int,input("enter a arr values:").split()))
search=int(input("enter a number:"))
found=False
for i in range(len(arr)):
    if arr[i]==search:
        found=True
        break

if found:
    print("element found")
else:
    print("not element found")
    