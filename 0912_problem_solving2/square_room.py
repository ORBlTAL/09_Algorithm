"""
NxN 정사각형이 주어진다면 각 방을 모두 돌면서 검사를 하긴 해야함
1번방에 왔으면 상하좌우 값들을 조사해서 자기보다 1 큰게 있는지 본다.
없으면 넘어가고, 있으면 그 방으로 이동해서 다시 조사, 큰게 있는지 본다.
-> 매 방에서 조사해서 cnt를 셈. (초기 cnt는 1) 각 cnt 값 중에서 가장 큰 값을 출력하면 될 듯?
----
cnt가 최대일 때의 방의 좌표는 어떻게 구해야 하나.....
"""

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def calc(i, j, count, si, sj):
    # 받아온 좌표를 토대로 델타순회 시작
    for k in range(4):
        nr, nc = i + dr[k], j + dc[k]
        if 0 <= nr < N and 0 <= nc < N:
            # 인접한곳의 값이 받아온 좌표에서의 값보다 1크면
            if arr[nr][nc] - 1 == arr[i][j]:
                # 그 때 재귀를 통해 해당 좌표로 이동, 거기서도 델타 연산을 해 위 조건을 만족하는지 찾음
                calc(nr, nc, count + 1, si, sj)
                return # 재귀 종료되고 바로 종료
    # for문을 다 돌고 나서는 계산된 count와 시작 좌표  si,sj를 저장
    path.append((count, si, sj))
    return # 함수 return 시켜서 종료

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = [] # count값과 시작 좌표 si, sj를 저장하는 path 리스트

    # 일단 모든 좌표를 돌아야 하니까 여기서 순회를 시작
    for i in range(N):
        for j in range(N):
            calc(i, j, 1, i, j)
    # count값은 최대로, si, sj의 경우에는 arr[i][j]가 가장 작은 경우여야 하니까 -를 붙여서 최소를 구함.
    best = max(path, key=lambda x: (x[0], -arr[x[1]][x[2]]))
    print(f'#{tc}', arr[best[1]][best[2]], best[0])
