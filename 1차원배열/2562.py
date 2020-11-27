import sys
init = int(sys.stdin.readline())
max = init
num = 1
for i in range(2,10):
    temp = int(sys.stdin.readline().rstrip())
    if max<temp:
        max = temp
        num = i
print(max)
print(num)
