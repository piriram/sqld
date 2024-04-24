# # 이렇게 하면 안됨
# boj_method = input.split
# a,b = boj_method()
# print(a,b)

# # input 메서드를 호출
# # 메서드 참조의 예시
# boj_method = input().split
# a,b = boj_method()
# print(a,b)

# # input 메서드를 호출의 예시
# a,b = input().split()

# 매번 예제입력을 터미널에 쓰기 번거로움으로 파일로 입력을 받아옴
# file_path = "10871.txt"
# file = open(file_path, "r") 
# file_content = file.read()
# file.close()    

# # print(file_content)


# a,b = file_content.splitlines() 

# # split에 아무것도 안넣으면 공백을 기준으로 나눔
# N,X = map(int, a.split())
# A = list(map(int, b.split()))

N,X = map(int, input().split())
A = list(map(int, input().split()))

for element in A:
    if element < X:
        print(element, end=" ")




