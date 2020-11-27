self_list = [False] + [True] *10000
def f(num):
    temp = str(num)
    std = len(temp)
    if std == 1:
        return 2*num
    if std == 2:
        return 11*temp[0] + 2*temp[1]
    if std == 3:
        return 101*temp[0] + 11*temp[1] + 2*temp[2]
    if std == 4:
        return 1001*temp[0] + 101*temp[1] + 11*temp[2] + 2*temp[3]

def erase(num):
    try:
        self_list[int(f(num))]
        while True:
            self_list[f(num)] = False
            num = f(num)
            if int(f(num)) > 10000 :
                break    
    except:
        return 0
    
for i in range(10001):
    erase(i)
for i in range(2,10001):
    if self_list[i]==True:
        print(i+1)
