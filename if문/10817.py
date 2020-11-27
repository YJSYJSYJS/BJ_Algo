a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a>=b:
    if c>=a:
        sec = a
    else:
        if c>=b:
            sec = c
        else:
            sec = b
else:
    if c>=b:
        sec = b
    else:
        if c>= a:
            sec = c
        else:
            sec = a
print(sec)
