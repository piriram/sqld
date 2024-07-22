def solution(sides):
    minimum = sides[0] if sides[0] < sides[1] else sides[1]
    answer = minimum * 2 - 1
    return answer


    