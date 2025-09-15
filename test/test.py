import sys
sys.stdin = open('input.txt')
T = int(input())

def dis(permu):
    global min_val
    val = 0
    val += (abs(permu[0][0]-0) + abs(permu[0][1] - 0))
    for i in range(N-1):
        val += abs(permu[i][0] - permu[i+1][0]) + abs(permu[i][1]- permu[i+1][1])
        if val>=min_val:
            return
    val += (abs(permu[N-1][0] - 0) + abs(permu[N-1][1] - 0))
    if val < min_val:
        min_val = val

def calc(depth,arr):
    if depth == N:
        dis(path)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            path.append(arr[i])
            calc(depth+1, arr)
            path.pop()
            visited[i] = False

for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False]*N
    path = []
    min_val = float('inf')
    calc(0,arr)
    print(f'#{tc}',min_val)