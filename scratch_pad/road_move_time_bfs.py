import sys
from collections import deque
sys.stdin = open('rmv.txt')
# 델타순회
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(grid, N, M):
    visited = [[-1]*M for _ in range(N)] # 방문 여부를 기록하기 위해 N*M visited 선언
    q = deque([(0, 0)]) # 큐 구현, 처음엔 시작좌표를 넣어줌
    visited[0][0] = 0 # 첫번째 시작이니 0으로
    while q:
        r, c = q.popleft() # 큐에 저장된 첫번째 위치의 좌표를 꺼내서 각각 r,c에 할당
        if r == N - 1 and c == M - 1: # 만약 r, c가 각각 N -1, M -1, 즉 끝점에 도달했으면
            return visited[r][c] # 함수 종료하면서 그떄의 visited[r][c]값을 반환
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i] # 델타 연산

            if (
                0 <= nr < N
                and 0 <= nc < M # 인덱스 범위
                and grid[nr][nc] == 1 # 이동하는 좌표안의 값이 1일 때만
                and visited[nr][nc] == -1 # 그리고 방문하지 않은곳만
            ):
                visited[nr][nc] = visited[r][c] + 1 # 다음 방문지는 현재 + 1 값을 저장
                q.append((nr, nc)) # 다음 방문지의 위치를 q에 넣어줌
    return -1 # 만약 성립되지 않는 상황이 생기면 -1을 반환


N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

print(bfs(grid, N, M))
