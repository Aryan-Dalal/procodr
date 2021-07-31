
#q6
arr = list()
for i in range(8):
    arr = list(map(int, input().split()))
    break

for z in arr:
    if arr.count(z) > 1:
        arr.remove(z)
print(arr)