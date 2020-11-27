ori = input()
cnt = 0
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
result = len(ori)
for c in cro:
    while c in ori:
        ori = ori.replace(c, '0')
        cnt+=1
print(len(ori))    
