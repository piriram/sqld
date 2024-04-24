# 괄호 문자열


# # 매번 예제입력을 터미널에 쓰기 번거로움으로 파일로 입력을 받아옴
# file_path = "1주차/9012.txt"
# file = open(file_path, "r") 
# file_content = file.read()
# file.close()    
# raw = file_content.splitlines()

# raw = list(input().splitlines())
# print(raw)
# # 입력 데이터의 수
# T = int(raw[0])
T = int(input())
stack = []

for i in range(0, T):
    line = input()
    size = len(line)
    for j in range(0,size):
        element = line[j]
        # print(element)
        if element == '(':
            stack.append('(')
        elif element == ')':
            if len(stack) == 0:
                stack.append('e') # 어차피 얘는 Valid PS가 아니므로 아무거나 넣어서 반복문을 빠져나감
                break
            else:
                stack.pop()
        else:
            print("에러발생")
        # print(stack)
    print("YES" if len(stack) == 0 else "NO")
    stack = [] # 스택 초기화