N = int(input())
words = list()
for i in range(N):
    words.append(input())
gn_cnt = 0

for word in words: # 단어 하나씩 순회
    is_gn = True # 아닌경우 False로 변경, 문자 순회완료 후 True유지 -> gn
    while i < len(word): # idx == 마지막 문자까지 순회
        num = word.count(word[i]) # 현재 문자의 개수 저장
        if num == 1: # 1개 밖에 없으면, 넘어가도 된다.
            i+=1
            continue
        else: # 2개 이상이면
            cnt = 1 # 연속된 개수를 세기 위한 변수 하나는 현재 문자이므로 1로 설정
            wls = list(word) # 문자들을 list에 하나씩 넣는다.
            std = word[i]
            while num !=cnt: # 같을 때까지 돌린다.(모두 연속될 경우)
                            # gn이 아닐 경우 달라도 반복문 종료되게 -> 다음 단어
                if word[i+cnt]!=std: # 연속될 경우  
                    cnt += 1 # cnt를 1증가
                    continue
                else: # 아직 num에 도달 하지 못했는데, 연속되지 않으면
                    is_gn=False # 이 단어는 gn일 수 없다!
                    break
            i = i + cnt # 연속되었을 경우 다른 문자열 부터 다시 순회하기 위해 설정    
    if is_gn:
        gn_cnt+=1
print(gn_cnt)

# N = int(input())
# words = list()
# for i in range(N):
#     words.append(input())
# gn_cnt = 0

# for word in words:
#     is_gn = True
#     while i < len(word):
#         num = word.count(word[i])
#         if num == 1:
#             i+=1
#             continue
#         else:
#             cnt = 1
#             wls = list(word)
#             std = word[i]
#             while num !=cnt:
#                 if word[i+cnt]!=std: 
#                     cnt += 1
#                     continue
#                 else:
#                     is_gn=False
#                     break
#             i = i + cnt
#     if is_gn:
#         gn_cnt+=1

                    

         
