def solution(array, commands):
    answer = []
    for i,j,k in commands:
        print(f"i:{i},j:{j},k:{k}")
        new_arr = sorted(array[i-1:j])
        print(new_arr)
        answer.append(new_arr[k-1])
    return answer