import sys
sys.stdin = open('input2.txt')

def calc(depth, N , k):
    global min_val

    # N 에 도달한경우 더이상 탐색할 수 없으므로 그때의 최소를 반환
    if depth == N:
        min_val = min(k, min_val)
        return
    # k가 min_val 보다 큰경우에는 이미 조건을 충족하지 못하므로 return 시킴
    if k >= min_val:
        return
    # 행은 depth +1,로 열은 for문으로 조회, state를 통해 같은 열은 조회 안하도록 함
    for i in range(N):
        if not state[i]:
            state[i] = True
            calc(depth+1, N, k + arr[depth][i]) # k에 각 좌표안의 값을 누적시킴. N=3될 때 가지의 값만 누적,
                                                # 재귀가 끝나면 이전에 일시정지 시킨 부분의 값으로 돌아감
            state[i] = False # 재귀가 끝나고 나서 False 처리

T = int(input())
for tc in range(1 , 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    state = [False] * N
    min_val = float('inf')
    calc(0, N, 0)
    print(f'#{tc}', min_val)


