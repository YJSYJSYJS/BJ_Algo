N = int(input())

def getHans(num):
    cnt = 0
    for n in range(100, num+1):
        n_str = str(n)
        d = int(n_str[0])-int(n_str[1])
        if d == int(n_str[1])-int(n_str[2]):
            cnt +=1
        else:
            continue
    return cnt

def CntHanNum(num):
    cnt = 0
    if num<100:
        cnt = num
    else:
        cnt = 99
        cnt += getHans(num)
    return cnt

print(CntHanNum(N))