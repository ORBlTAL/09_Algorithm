import sys
from collections import deque
sys.stdin = open('fi.txt')
# 섬을 찾기위한 8방향 델타
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def bfs(grid, N, M, start_r, start_c):
    q = deque([(start_r, start_c)]) # q에 시작지점 좌표를 넣어줌
    visited[start_r][start_c] = True # 시작지점은 섬이 확실하므로 True 해줘서 방문처리
    while q: # q가 다 빌때까지
        r, c = q.popleft() # q에 넣어둔 좌표를 가져옴
        for i in range(8): # 델타 순회 시작
            nr, nc = r + dr[i], c + dc[i]
            if (
                0 <= nr < N
                and 0 <= nc < M # 인덱스 범위 방지
                and grid[nr][nc] == 1 # 값이 1이고 (섬이고)
                and not visited[nr][nc] # 아직 방문 처리가 안돼어있으면
            ):
                visited[nr][nc] = True # 해당 부분을 True 처리해주고
                q.append((nr, nc)) # 다음좌표 델타 연산을 위해 q에 nr, nc 대입
    # return visited

N, M = map(int, input().split())
grid = [list(map(int, input()))for _ in range(N)]
visited = [[False]*M for _ in range(N)] # 섬위치를 나타내는 좌표에서 방문처리를 계산하기 위한 N*M 배열 선언
island_cnt = 0 # 섬의 개수를 세는 카운터
# for i in grid:
#     print(i)
for i in range(N): # 섬 좌표 순회
    for j in range(M):
        if grid[i][j] == 1 and not visited[i][j]: # 값이 1이고, 아직 방문하지 않았을 때
            bfs(grid, N, M, i, j) # 그때 bfs 탐색 시작. 해당 좌표를 넣어줌
            island_cnt += 1 # bfs 동작이 실행되면 섬을 발견한 것이므로 카운트 해줌

# for i in visited:
#     print(i)

print(island_cnt)