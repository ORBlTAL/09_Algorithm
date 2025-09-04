# import sys
# # from itertools import permutations
# from pprint import pprint
# sys.stdin = open('input3.txt')
# T = int(input())
#
# for tc in range(1, 1 + T):
#     N = int(input())
#     arr = [list(map(int, input().split()))for _ in range(N)]
#     k = [i for i in range(1,N)]
#     result = []
#     k = list(range(N))
#     for i in range(1, N):  # 1부터 시작 → 자기 자신 제외
#         rotated = k[i:] + k[:i]
#         result.append(rotated)
#
#     min_val = float('inf')
#     for j in range(N-1):
#         sum = 0
#         for i in range(N):
#             sum += arr[i][result[j][i]]
#         print(sum)
#         min_val = min(sum,min_val)
#     # print(min_val)


import sys
from itertools import permutations
sys.stdin = open('input3.txt')
T = int(input())

for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    nodes = [i for i in range(1, N)]  # 0인 부분들은 제외
    min_val = float('inf')

    for perm in permutations(nodes):  # (N-1)! 경우 생성
        sum_val = 0
        pos = 0  # 시작은 사무실 이므로 0

        # 순열대로 방문
        for next in perm:
            sum_val += arr[pos][next]
            pos = next # 서로 좌표간에 연결성을 이용, next 좌표가 현재 좌표로

        sum_val += arr[pos][0] # 마지막에는 무조건 사무실로 오므로

        min_val = min(min_val, sum_val) # 최소 구하기

    print(f"#{tc} {min_val}")
