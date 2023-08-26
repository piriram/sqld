# minumum : 최소 필요 피로도
# consume : 소모 피로도
# 목적 : 최대한 많은 던전 탐험
# dfs -> 최단거리/네트워크/조합에서 사용
# 0 -> 1 -> 2 이렇게 순차적으로 가는게 아니라 1->0->2도 가능함을 고려해야함
# 

def solution(k, dungeons):
    global answer,d_size,visited
    answer = -1
    d_size = len(dungeons)
    visited = [False] * d_size
    for i in range(d_size):
        visited[i] = True
        dfs(k,dungeons,i,0)
        visited[i] = False
    return answer

def dfs(k,dungeons,index,ans):
    global answer,d_size,visited
    
    if index >= d_size: # 던전의 마지막 방을 벗어나면 dfs 종료
        return
    else:
        # 이부분에 진입하면 최대 던전 방문수를 갱신할 수 있는 지 조사
        if dungeons[index][0] <= k: # 최소 필요 피로도보다 현재 체력이 크거나 같아야 던전에 진입 가능    
            answer = max(answer,ans+1)
            for i in range(d_size):
                if visited[i] == False :
                    visited[i] = True
                    dfs(k-dungeons[index][1],dungeons,i,ans+1)
                    visited[i] = False
                
                
            return
    
    