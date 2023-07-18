def solution(citations):
    ct = citations
    answer = 0
    
    citations.sort(reverse=True)
    num = 0
    print(citations)
    for ct in citations:
        num=ct
        if answer >= num:
            break
        answer += 1
    return answer