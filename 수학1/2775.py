import copy
T = int(input())
for t in range(T):
    k = int(input())
    n = int(input())
    pops = [i for i in range(1, n+1)]
    for i in range(k):
        sum = 0
        next_pop = list()
        for j in range(n):
            sum += pops[j]
            next_pop.append(sum)
        pops = copy.deepcopy(next_pop)
    print(sum)
    
#     r_num = list()
#     1 2 3 4 ... n
#     -------------
# '0' 1 2 3 4 ... n
# '1' 1 3 6 10
# '2' 1 4 10 20
# '3' 1 5 15 35
# '4' 1 6 21 56
# '5' 1 7 28 84
# ...
# 'k' 1 8

# a[0,n] = n
# a[k,1] = 1
# a[k,2] = k+2 
# a[k,n] = k + 3 + sum_{n=3}^{n}a[k-1,n] 
# = k + 3 + a[k-1,3]  + a[k-1,4] + a[k-1,5] + ... + a[k-1,n]
# = k+3 + (k-1)+3+a[k-2,3]