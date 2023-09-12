# 마라톤 -> 완주못한 한명
def solution(participant, completion):
    answer = ''
    par_dic = {}
    com_dic = {}
    par_len,com_len = len(participant),len(completion)\
    
    # 참가자 딕셔너리와 완주자 딕셔너리 만드는 과정
    for i in range(com_len):
        par = participant[i]
        com = completion[i]
        if par in par_dic:
            par_dic[par] += 1
        else:
            par_dic[par] = 1
        if com in com_dic:
            com_dic[com] += 1
        else:
            com_dic[com] = 1
    for i in range(com_len,par_len):
        par = participant[i]
        if par in par_dic:
            par_dic[par] += 1
        else:
            par_dic[par] = 1
            
    # 1명의 미완주자 찾기
    for par in par_dic.keys():

        if not par in com_dic or par_dic[par] != com_dic[par]:
            answer = par
            
            
    return answer

#     for person in participant:
#         if not person in completion:
#             answer = person
#             break
            
    # 실패 : 두명이 참가하였으나 한명만 완주한 경우 처리 불가 and 시간복잡도 n^2이므로 효율성테스트에서 시간초과