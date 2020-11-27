N = int(input())
words = list()

for i in range(N):
    words.append(input())

gn_cnt = N

for word in words:
    wl = list(word)
    for i in range(len(wl)):
        std = wl[i]
        idx = i
        if str(wl[i]).isdigit()==False:
            for j in range(i, len(wl)):
                if wl[j] == std:
                    wl[j] = idx
        else:
            continue    
    for j in range(len(wl)-1):
        if wl[j+1] - wl[j] < 0:
            gn_cnt-=1 
            break

print(gn_cnt)