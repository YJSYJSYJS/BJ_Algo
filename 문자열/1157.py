word = input()
word = word.upper()
ls = dict()
for w in word:
    if w in ls.keys():
        ls[w] += 1
    else:
        ls[w] = 1

max = 0
draw = bool()
for l in ls.keys():
    if ls[l]>max:
        max = ls[l]
        result = l
        draw = False
    elif ls[l]==max:
        draw = True
    else:
        continue

if draw:
    print('?')
else:
    print(result)
