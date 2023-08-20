# A,B는 자연수
# a * b (a,b는 각각 A,B 배열의 임의의 선택된 수)
import numpy as np
def solution(A,B):
    answer = 0
    A = np.sort(A)[::-1]
    B = np.sort(B)

    for i in range(len(A)):
        sum = int(A[i]*B[i])
        answer += sum

    return answer