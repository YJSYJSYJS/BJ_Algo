X = int(input())
cnt = 1
sum = 0
right = True
while True:
    if X<sum+cnt+1: 
        break
    sum += cnt
    cnt += 1
    
d = X - sum
par = str(cnt - d + 1)
child = str(d)
if cnt % 2 ==1:
    print(par+'/'+child)
else:
    print(child+'/'+par)
