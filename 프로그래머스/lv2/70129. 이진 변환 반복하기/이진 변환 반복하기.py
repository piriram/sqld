
answer = [1,0]
def solution(s):
    s_len = test(s)
    
    while s_len>1:
        answer[0] += 1
        s_len = test(bin(s_len)[2:])
    return answer
def test(s):
    word = ''
    for char in s:
        if char == "1":
            word+="1"
        elif char =='0':
            answer[1] += 1 
        else:
            print("0과 1이 아닙니다")
    return len(word)
    # print(word)
            
        