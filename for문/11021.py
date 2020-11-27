import sys
t = int(sys.stdin.readline())
sum = []
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    sum.append(a+b)
a = 0
for s in sum:
    a+=1    
    print("Case #{}: {}".format(a, s))
    