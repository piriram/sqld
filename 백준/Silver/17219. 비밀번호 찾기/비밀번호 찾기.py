N,M = map(int,input().split())
세뚜 = {}
for i in range(N):
    a,b = input().split()
    # print(a)
    # print(b)
    세뚜[a]=b

for i in range(M):
    key = input()
    print(세뚜[key])