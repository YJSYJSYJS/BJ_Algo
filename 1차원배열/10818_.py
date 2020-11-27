import sys
n = int(sys.stdin.readline())
item = list(map(int, sys.stdin.readline().split()))
max = item[0]
min = item[0]
for i in item:
    if i > max:
        max = i
    if i < min:
        min = i
print(min, max)
