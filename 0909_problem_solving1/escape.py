"""
1. BFS로 접근
    - 이동 방향 : 상하좌우
    - 이동이 불가능한 케이스 발생 -> continue로 처리하면 편함
     - [델타 배열 기본] 범위 밖으로 나가면 못감
     - [방문 기록 기본] 이미 방문한 곳은 못감
     - [0이면 못간다]
     - [문제 조건]
        - 현재 내 위치에서 뚫려있는 곳만 이동 가능
        - 다음 위치의 입구가 뚫려있는 곳으로만 가능
         -> 이런 케이스들은 델타 배열과 동일한 순서(상하좌우)
                이동 가능 여부를 기록해두면 좋다.

2. 방문 기록을 해야한다. (visited)
"""
from collections import deque
import sys
sys.stdin = open('input3.txt')
T = int(input())
# 델타 배열 / 순서는 상 하 좌 우
dr = [-1, 1, 0, 0] # y
dc = [0, 0, -1, 1] # x
# 터널 종류에 따른 이동 가능 여부 기록 / 순서는 상 하 좌 우.
types = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

def bfs(R, C):
    # q = [(R, C)] # 후보군
    q = deque([(R,C)])
    visited[R][C] = 1 # 출발점 초기화
    while q: # 후보군이 없을 때 까지( 더 이상 방문할 수 있는 곳이 없으면 종료)
        # now_y, now_x = q.pop(0)
        now_y , now_x = q.popleft()
        dirs = types[arr[now_y][now_x]]

        for dir in range(4):# 상하좌우 확인
            # 출구가 없으면 다음 방향 확인(continue)
            if dirs[dir] == 0:
                continue
            # 다음 좌표
            new_y = now_y + dr[dir]
            new_x = now_x + dc[dir]

            # 범위 밖이면 pass
            if new_y < 0 or new_y >= N or new_x < 0 or new_x >= M:
                continue

            # 못가는 곳이면 pass
            if arr[new_y][new_x] == 0:
                continue

            # 이미 방문했으면 pass
            if visited[new_y][new_x]:
                continue

            # 다음 좌표 터널 뚫린 것을 확인
            next_dirs = types[arr[new_y][new_x]]
            # 현재 상좌 -> next_dirs가 하우가 안뚫렸으면 못감
            if dir % 2 == 0 and next_dirs[dir+1] == 0:
                continue

            # 현재 하우 -> next_dirs의 상좌가 안뚫렸으면 못감
            if dir % 2 == 1 and next_dirs[dir-1] == 0:
                continue

            # L 시간 이후는 볼 필요 없다
            if visited[now_y][now_x] + 1 > L:
                continue

            # 시간을 +1 해주면서 기록
            visited[new_y][new_x] = visited[now_y][now_x] + 1
            q.append((new_y, new_x))

for tc in range(1, 1 + T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    # 방문 여부에 특정 좌표까지 몇 시간이 걸렸는 지 기록
    visited = [[0] * M for _ in range(N)]
    bfs(R, C)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                cnt +=1
    print(f'#{tc} {cnt}')
