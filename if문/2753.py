# 윤년 기준
#  1. 4의 배수
#  2. 100의 배수가 아니거나 400의 배수\

y = input()
y = int(y)
is_leap = 0
if y%4==0:
    if y%100!=0:
        is_leap=1
    if y%400==0:
        is_leap=1
print(is_leap)
