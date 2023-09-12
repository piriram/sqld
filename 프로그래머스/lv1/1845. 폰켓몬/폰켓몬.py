def solution(arr):
    hi = set(arr)
    print(hi) # 카운팅 정렬을 쓰지 않고 빠르게 하는 방법 -> 종류들을 집합처리
    
    return min(len(arr)/2, len(set(arr)))

# # N/2개 수집할 때 최대한 많은 종류의 폰켓몬 수집
# # 계수정렬?
# # best -> 하나씩만 가져가기
# # 1이상인 것이 n/2개가 되는지 확인
# # 1 이상인 것의 갯수 : valid_index
# # n/2 
# import math
# def solution(nums):
#     answer = 0
#     n = len(nums)
#     counting = dict()
#     for i in nums:
#         if i in counting:
#             counting[i] += 1
#         else:
#             counting[i] = 1
#     sorted_counting = sorted(counting.items(), key=lambda x: x[0])
    
#     size = len(sorted_counting)
    
#     if (n/2)<=size: 
#         # 가져가는 개수<=전체 종류 => 종류당 하나씩 총 n/2 종류 가져감
#         answer = n/2
#     else: 
#         # 가져가는 개수 > 전체 종류 => 중복되는 종류 있으므로 전체 종류는 종류 개수가 됨
#         answer = size
#     return answer
