total = list(range(1, 10001))
target = list(range(1, 10001))

def SumDel(num):
    num_str = str(num)
    sum = num
    for n in num_str:
        sum+=int(n)
    if sum in target:
        target.remove(sum)
        return SumDel(sum)
    else:
        return 0

for t in total:
    if t in target:    
        SumDel(t)
    else:
        continue

for t in target:
    print(t)