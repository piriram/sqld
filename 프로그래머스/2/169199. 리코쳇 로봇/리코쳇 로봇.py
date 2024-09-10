from collections import deque

def solution(board):
    grid = [list(row) for row in board]
    start, final = finder(grid)
    
    # start, final이 None이면 -1을 리턴
    if start is None or final is None:
        return -1

    return bfs(start, final, grid)

def bfs(start, final, grid):
    queue = deque([(start[0], start[1], 0)])  # (row, col, steps)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    row_len = len(grid)
    col_len = len(grid[0])
    visited = [[False] * col_len for _ in range(row_len)]  # 방문 기록
    visited[start[0]][start[1]] = True  # 시작점 방문 처리

    while queue:
        # 큐에서 가장 왼쪽에 있는 좌표와 step 수를 가져옴
        a, b, step = queue.popleft()
        
        # 목표에 도착하면 step 수 반환
        if (a, b) == final:
            return step

        # 네 방향으로 이동
        for dir in directions:
            new_a, new_b = a, b
            
            # 장애물 'D'를 만나기 전까지 이동
            while 0 <= new_a < row_len and 0 <= new_b < col_len and grid[new_a][new_b] != 'D':
                new_a += dir[0]
                new_b += dir[1]
            
            # 범위를 벗어나거나 장애물 앞에서 멈춤 (이동한 마지막 유효 위치로 한 칸 되돌림)
            new_a -= dir[0]
            new_b -= dir[1]

            # 방문하지 않았고 이동할 수 있는 위치이면 큐에 추가
            if not visited[new_a][new_b]:
                visited[new_a][new_b] = True
                queue.append((new_a, new_b, step + 1))

    return -1  # 목표에 도달하지 못한 경우

def finder(grid):
    start = None
    final = None
    for a in range(len(grid)):
        for b in range(len(grid[a])):
            if grid[a][b] == 'R':
                start = (a, b)  # 시작점 좌표
            if grid[a][b] == 'G':
                final = (a, b)  # 목표점 좌표
    return start, final
