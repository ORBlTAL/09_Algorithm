import sys
sys.stdin = open('input4.txt')

def calc(depth, k):
    global val
    if k <= val: # 확률이므로 곱해질수록 작아지는데 이미 val보다 작으면 최대 확률이 아니므로 return 시킴
        return
    if depth == N: # N 까지 도달하면 그때의 확률값이 최대인지 판단
        val = max(k, val)
        return
    # i로는 열 순회 , depth로 행 순회, state로 같은열 안고르게끔 bool 판단
    for i in range(N):
        if not state[i]:
            state[i] = True
            calc(depth + 1, k*arr[depth][i]*0.01) # k에 누적할 때는 확률이므로 0.01을 곱해서 넘김
            state[i] = False

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    state = [False] * N
    val = 0
    calc(0, 1.0) # 곱이므로 1.0을 k에 초기로 할당
    print(f'#{tc} {val * 100:.6f}') # 퍼센트 단위이므로 100을 곱해주고, 소수점 6자리 까지만 나오도록 .6f

