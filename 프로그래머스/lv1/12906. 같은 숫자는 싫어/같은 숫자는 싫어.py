# input : arr
# 0~9의 값을 원소로 가지는 배열(중복 o)
# 중복제거하여 출력
# 중복시 앞에 것을 남김
def solution(arr):
    answer = []
    # arr = sorted(arr)
    tmp1=tmp2=0

    for i in range(0,len(arr)):
        if arr[i]==0 and tmp2==0:
            tmp1=arr[i]
            tmp2+=1
            answer.append(arr[i])
        elif arr[i]==tmp1:
            tmp2+=1
        else:
            tmp1=arr[i]
            answer.append(arr[i])
    return answer