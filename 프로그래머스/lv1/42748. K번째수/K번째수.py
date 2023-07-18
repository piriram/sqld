# i~j 크롭
# k번째 있는 수 -> i+k
def solution(array, commands):
    answer = []
    for cmd in commands:
        i,j,k = cmd
        clc = sorted(array[i-1:j])
        answer.append(clc[k-1])

    return answer