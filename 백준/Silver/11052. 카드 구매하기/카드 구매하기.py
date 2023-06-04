# 카드의 개수
N = int(input())

# 카드팩의 가격 P 입력, 0은 인덱스 맞추기 위해
P = [0] + list(map(int, input().split()))

# dp 리스트 초기화, dp[i]는 i개의 카드를 구매할 때 지불할 최대 금액
dp = [0] * (N+1)

for i in range(1, N+1):

    for j in range(1, i+1):
        # i-j개 카드의 최대 가격 + j개 카드팩 가격) 중 더 큰 값
        dp[i] = max(dp[i], dp[i-j] + P[j])

# 카드 N개를 구매할 때의 최대 가격 출력
print(dp[N])
