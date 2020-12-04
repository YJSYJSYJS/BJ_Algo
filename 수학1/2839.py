N = int(input())

fives = 0
threes = 0

while True:
    if 5*(fives+1)<=N:
        fives+=1
    else:
        break

d = N - (3*threes + 5*fives)

if d%3 == 0:
    threes = int(d/3)
elif d%3 ==1:
    threes = int(d/3) + 2
    fives = fives-1
else:
    threes = int(d/3) + 4
    fives = fives-2

if fives<0:
    print(-1)
else:
    print(fives + threes)
