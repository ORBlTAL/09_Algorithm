import sys
from collections import deque
sys.stdin = open('rmv.txt')

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def detect(x,y):
    global cnt
    global min_val
    if x == 3 and y == 5:
        min_val = min(cnt, min_val)
        return
    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]
        if 0<=nr<N and 0 <=nc<M:
            if grid[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                cnt +=1
                detect(nr, nc)
                cnt -=1
                visited[nr][nc] = False

N, M = map(int,input().split())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
cnt = 0
min_val = 100
visited[0][0] = True

detect(0,0)
print(min_val)





















































