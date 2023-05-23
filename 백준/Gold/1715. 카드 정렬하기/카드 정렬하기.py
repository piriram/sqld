import heapq

N = int(input())
queue = []
for _ in range(N):
    heapq.heappush(queue, int(input()))

result = 0
while len(queue) != 1:
    num1 = heapq.heappop(queue)
    num2 = heapq.heappop(queue)
    sum_val = num1 + num2
    result += sum_val
    heapq.heappush(queue, sum_val)

print(result)
