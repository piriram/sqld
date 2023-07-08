# s.title()로 할 시 3obj가 3Obj로 반환되어 틀림
def solution(s):
    answer = []
    words = s.split(' ')  # 문자열을 공백을 기준으로 단어로 분리

    for word in words:
        if word:  # 단어가 비어있지 않은 경우
            word = word[0].upper() + word[1:].lower()  # 첫 글자는 대문자, 나머지는 소문자로 변환
        answer.append(word)

    return ' '.join(answer)  # 단어들을 공백으로 연결하여 반환

