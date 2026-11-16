data = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40,
    "e": 50
}

largest = None
second = None

for key in data:
    num = data[key]
    print(num)

    if largest is None or num > largest:
        second = largest
        largest = num

    elif num != largest and (second is None or num > second):
        second = num

print("Largest:", largest)
print("Second largest:", second)