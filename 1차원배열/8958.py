import sys
t = int(sys.stdin.readline())
combo = []
oxs = []
score = []
for i in range(t):
    temp = list(sys.stdin.readline())
    oxs.append(temp)
    combo.append(0)
    score.append(0)
    for ox in oxs[i]:
        if ox=='O':
            combo[i] += 1
            score[i] += combo[i]    
        else:
            combo[i] = 0
for s in score:
    print(s)


