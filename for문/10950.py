n = int(input())
sums = []
for case in range(n):
    a, b = map(int,input().split())
    sums.append(a+b)
for s in sums:
    print(s)
