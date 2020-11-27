import sys
n = int(sys.stdin.readline())
item = list(map(int, sys.stdin.readline().split()))
print(min(item), max(item))
