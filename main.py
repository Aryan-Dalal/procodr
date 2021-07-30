#put n space seperated integers into array
#arr = list(map(int, input().split()))

#put letters or digits of a word or number into array
#WORD
#list(word)
#Number
#arr = [int(x) for x in str(number)]

# taking input on the same line
#n,m = [int(x) for x in input().split()]

#PROBLEM
# Now that Chef has finished baking and frosting his cupcakes, it's time to package them. 
# Chef has N cupcakes, and needs to decide how many cupcakes to place in each package. 
# Each package must contain the same number of cupcakes. 
# Chef will choose an integer A between 1 and N, inclusive, and place exactly A cupcakes into each package. 
# Chef makes as many packages as possible. Chef then gets to eat the remaining cupcakes. Chef enjoys eating cupcakes very much. 
# Help Chef choose the package size A that will let him eat as many cupcakes as possible.

# Input
# Input begins with an integer T, the number of test cases. Each test case consists of a single integer N, the number of cupcakes.

# Output
# For each test case, output the package size that will maximize the number of leftover cupcakes. 
# If multiple package sizes will result in the same number of leftover cupcakes, print the largest such size.

# Sample Input
# 2
# 2
# 5

# Sample Output
# 2
# 3

import math
t = int(input())
test_cases = []
ans = []
for z in range(t):
  test_cases.append(input())
  ans.append(int(test_cases[z]) // 2 + 1)
print("\n")

for i in range(len(ans)):
  print(ans[i])
# i = 0
# while i<t:
  
#   i = i+1
