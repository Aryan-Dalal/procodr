arr = [12, "Val", 567.56, "ProCodr", "156", 23]
print("input: ", arr)

def swap(arr, x, y):
    arr[x], arr[y] = arr[y], arr[x]

for i in range(0, len(arr), 2):
    swap(arr, i, i+1)

print("Output: ",arr)

