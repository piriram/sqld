def solution(n):
    answer = 0
    try_num = 1 #반복문을 돈 횟수
    while try_num<=n:
        try_num += 1
        answer+=1
        
        while answer%3 == 0 or '3' in str(answer):
            answer += 1
              
    return answer