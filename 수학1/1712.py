A, B, C = list(map(int, input().split()))
# BEP=0
# cost = A + B*BEP
# prof = C*BEP

# while cost>=prof:
#     BEP+=1
#     cost = A+B*BEP
#     prof = C*BEP
if B!=C:
    BEP = int(A/(C-B))+1
else:
    BEP = -1
    
if BEP > 0:
    print(BEP)
else:
    print(-1)