# # brute force 
# arr = [5, 8, 2, 9]
# target = 2

# for i in range(len(arr)):
#     if arr[i] == target:
#         print("Position =", i + 1)


# better


# arr = [5, 8, 2, 9]
# target = 2

# for index, value in enumerate(arr):
#     if value == target:
#         print("Position =", index + 1)
#         break



# optimal

def find_position(arr, target):

    for i in range(len(arr)):

        if arr[i] == target:
            return i + 1

    return -1


arr = [5, 8, 2, 9]
target = 2

result = find_position(arr, target)

if result != -1:
    print("Position =", result)
else:
    print("Element not found")