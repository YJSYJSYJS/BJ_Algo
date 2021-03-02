T = int(input())
answers = list()
for i in range(T):
    H, W, N = map(int, input().split())
    floor = N%H
    r_num = N//H + 1
    if floor == 0:
        floor = H
        r_num-=1
    ans = floor*100 + r_num
    print(str(ans))  
    