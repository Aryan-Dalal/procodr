t = 4
arr = []
ans = 0
i = 0
while i<t:
    arr = list(map(int, input().split()))
    ans = sum(arr)
    i = i+1
    break
print(ans)