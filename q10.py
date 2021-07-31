#put n space seperated integers into array
#arr = list(map(int, input().split()))

#put letters or digits of a word or number into array
#WORD
#list(word)
#Number
#arr = [int(x) for x in str(number)]

# taking input on the same line
#n,m = [int(x) for x in input().split()]



s = input()
arr = list(s.lower())
ans = []
for i in arr:
    if arr.count(i) > 1:
        if i not in ans:
            ans.append(i)

for z in ans:
    print(z)


