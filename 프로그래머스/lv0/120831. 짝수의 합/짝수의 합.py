def solution(n):
    answer = 0
    d = 2
    a = 2
    if n % 2 == 1:
        n -= 1
    num = int(n/2)
    answer = num*(a+n)/2
    
    return answer 