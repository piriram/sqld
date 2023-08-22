def solution(n):
    answer = test(n)
    return answer
def test(target):
    ans = 0
    sum = 0
    a = 1
    while a <= target:
        b = a # 연속 찾기 숫자
        while True:
            sum += b
            if sum == target:
                ans += 1
                break
            elif sum > target:
                break
            else:
                b += 1 # 1 증가
        a += 1 # 다음 시작 값 찾기
        sum = 0 # 자연수의 합 초기화
        
    return ans