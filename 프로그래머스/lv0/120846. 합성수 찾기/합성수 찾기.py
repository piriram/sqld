# 소수가 아닌 수를 찾아라
def solution(n):
    answer = 0
    for num in range(4,n+1):
        if not isPrime(num):
            answer += 1
    return answer

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def yaksu_find(n): #약수를 찾는 함수(공부용으로 한번 짜봤음),소수 찾는게 더 빠를듯
    div = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            div.append(i)
            if (n//i) != i:
                div.append(n//i)
        
                
    return sorted(div)
    