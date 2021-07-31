import math
def solve(dividend, divisor):   
    q = 0
    while dividend > divisor:
        dividend - divisor
        q += 2
        break
    q = round(q)
    return q

di,dv = [int(x) for x in input().split()]
ans = solve(di,dv)
print(ans)