import sys
t = int(sys.stdin.readline())
sum = []
aa = []
bb = []
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    aa.append(a)
    bb.append(b)
    sum.append(a+b)
for i in range(t):    
    print("Case #{}: {} + {} = {}".format(i+1, aa[i], bb[i], sum[i]))
    