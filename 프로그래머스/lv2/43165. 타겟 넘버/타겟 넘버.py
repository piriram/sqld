from collections import deque
def solution(numbers, target):
    answer = 0
    que = deque()
    n=len(numbers)
    que.append([numbers[0],0])
    que.append([-1*numbers[0],0])
    while que:#큐가 비어있지 않는동안 실행
        tmp,idx = que.popleft()
        idx += 1
        if idx<n:
            que.append([tmp+numbers[idx],idx]) 
            que.append([tmp-1*numbers[idx],idx])
            
        else:
            if tmp == target:
                answer += 1
    return answer