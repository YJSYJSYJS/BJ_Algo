import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
mul = a*b*c
mul = str(mul)
for i in range(10):
    print(mul.count(str(i)))          
