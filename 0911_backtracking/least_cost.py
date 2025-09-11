# import sys
# sys.stdin = open('input2.txt')
# T = int(input())
#
# def calc(k):
#     global sum_val
#     sum_val +=k
#
# def judge(cnt):
#     if cnt == N:
#         return
#     for j in range(N):
#         if not state[cnt][j]:
#             state[cnt][j] = 1
#             calc(arr[cnt][j])
#             judge(cnt + 1)
#             state[cnt][j] = 0
#
#
# for tc in range(1, 1 + T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     state = [[0]*N for _ in range(N)]
#     sum_val = 0
#     judge(0)
#     print(sum_val)
#

import sys
sys.stdin = open('input2.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # --- Hungarian algorithm (minimization), 1-indexed internal arrays ---
    n = N
    u = [0] * (n + 1)  # potentials for rows
    v = [0] * (n + 1)  # potentials for columns
    p = [0] * (n + 1)  # p[j] = matched row for column j
    way = [0] * (n + 1)

    i = 1
    while i <= n:
        p[0] = i
        j0 = 0
        used = [False] * (n + 1)
        minv = [10**9] * (n + 1)
        way = [0] * (n + 1)

        j = 0
        used[j0] = True
        while True:
            i0 = p[j0]
            delta = 10**9
            j1 = 0

            j = 1
            while j <= n:
                if not used[j]:
                    cur = arr[i0 - 1][j - 1] - u[i0] - v[j]
                    if cur < minv[j]:
                        minv[j] = cur
                        way[j] = j0
                    if minv[j] < delta:
                        delta = minv[j]
                        j1 = j
                j += 1

            k = 0
            while k <= n:
                if used[k]:
                    u[p[k]] += delta
                    v[k] -= delta
                else:
                    minv[k] -= delta
                k += 1

            j0 = j1
            used[j0] = True

            if p[j0] == 0:
                break

        # augmenting
        while True:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
            if j0 == 0:
                break

        i += 1

    # 최소 비용 계산
    total = 0
    j = 1
    while j <= n:
        total += arr[p[j] - 1][j - 1]
        j += 1

    print(f"#{tc} {total}")

