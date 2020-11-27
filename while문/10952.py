import sys
sum = []
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==0&b==0:
        break
    sum.append(a+b)
for s in sum:
    print(s)
    