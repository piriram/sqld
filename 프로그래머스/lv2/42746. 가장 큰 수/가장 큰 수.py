def solution(numbers):
    # 정수를 문자열로 변환하여 문자열 배열로 저장
    numbers = list(map(str, numbers))
    
    # 비교 함수를 정의하여 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)

    # 정렬된 문자열 배열을 이어붙여서 하나의 문자열로 만듦
    answer = ''.join(numbers)
    
    # 문자열이 "0"으로만 구성되어 있는 경우 처리
    if answer[0] == '0':
        answer = '0'
    
    return answer
