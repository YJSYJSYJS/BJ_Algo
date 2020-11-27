import sys
n, x = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
for i in s:
    if i<x:
        print(i, end=" ")

