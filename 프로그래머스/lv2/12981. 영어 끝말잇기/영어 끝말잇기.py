# 끝말잇기에서 탈락하는 사람을 찾아라
def solution(n, words):
    answer = [0,0]
    used = set()
    used.add(words[0])
    for i in range(len(words)):
        
        if (i+1) != len(words):
            if (words[i+1] in used) or (words[i][-1] != words[i+1][0]):
                print(words[i+1])
                if (i+2)%n == 0:
                    answer[0]=n
                else:
                    answer[0]=(int((i+2)%n))
                if (i+2) % n == 0:
                    answer[1]= (i+2)//n
                else:
                    answer[1]=((i+2)//n)+1
                    
                print(f"i={i+2},{words[i][-1]}와 {words[i+1][0]}")
                break
            else:
                used.add(words[i+1])
                # print(words[i])
        

    return answer