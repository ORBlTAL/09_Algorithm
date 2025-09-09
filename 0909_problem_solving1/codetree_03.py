import sys
sys.stdin = open('input_ct_3.txt')
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt2 = 0
for r in range(N):
    for c in range(N):
        cnt = 0
        for k in range(4):
            nr , nc = r+dr[k] , c+dc[k]
            if 0<=nr<N and 0<=nc<N:
                if arr[nr][nc] == 1:
                    cnt+=1
                    # print(cnt)
        if cnt >= 3:
            cnt2 +=1
print(cnt2)
