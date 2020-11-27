import sys
t = int(input())
elite_per = []
for i in range(t):
    elite_num = 0
    n = list(map(int, sys.stdin.readline().split()))
    avg = (sum(n)-n[0])/(len(n)-1)
    for i in range(1,n[0]+1):
        if n[i]>avg:
            elite_num += 1
    elite_per.append(round(elite_num/n[0]*100, 3))
for e in elite_per:
    print ("%.3f%%" % e)
