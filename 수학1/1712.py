A, B, C = list(map(int, input().split()))
# BEP=0
# cost = A + B*BEP
# prof = C*BEP

# while cost>=prof:
#     BEP+=1
#     cost = A+B*BEP
#     prof = C*BEP

# print(BEP)

print(int(A/(C-B))+1)