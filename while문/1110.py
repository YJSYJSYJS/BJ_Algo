import sys
n = list(map(int, sys.stdin.readline().rstrip()))
if len(n)<2:
    n.insert(0, 0)
init = n[0]*10+n[1]
i=0
while True:
    s = sum(n)
    n[0]=n[1]
    n[1]=s%10
    i+=1
    if n[0]*10+n[1] == init:
        break
print(i)
    