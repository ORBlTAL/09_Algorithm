import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    cnt = 0
    for i in range(N):
        if arr[0][i] != arr[1][i]:
            cnt +=1
            for j in range(N):
                if arr[0][j] == 1:
                    arr[0][j] -=1
                elif arr[0][j] == 0:
                    arr[0][j] +=1
    print(f'#{tc}',cnt)


