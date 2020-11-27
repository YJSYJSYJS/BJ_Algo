import sys
rem = set()
for i in range(10):
    num = int(sys.stdin.readline())
    rem.add(num%42)
print(len(rem))
