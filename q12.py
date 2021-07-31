chars = list(input())

lmat = [[None, None, None, None, None],[None, None, None, None, None],[None, None, None, None, None],[None, None, None, None, None],[None, None, None, None, None]]
c = 0
for i in range(5):
    for j in range(5):
        lmat[j][i] = chars[c]
        c += 1
print(lmat)

for i in range(5):
    for j in range(5):
        print(lmat[i][j], end="")