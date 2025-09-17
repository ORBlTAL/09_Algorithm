"""
사과를 수확하는 순서를 결정해 최소 이동거리를 구하는 문제
사과를 수확하는 순서에 따라 거리가 달라지므로, 순열로 접근해야 할 것 같음
사과들 간에 거리를 구하는 과정 + (0,0)좌표에서 첫 사과의 거리와 마지막 사과와 (0,0)사이의 거리를 더해줘야함
각각의 이동거리 결과들중에서의 최소값을 구해서 최종 출력
"""

import sys
from itertools import permutations # 순열을 사용하기 위해 itertools 라이브러리 불러옴
sys.stdin = open('input2.txt')

def calc(permu):
    global min_val # 최소값을 구하기 위해 글로벌로 선언
    val = 0 # 이동거리 초기값 val을 0으로 선언
    val += (abs(permu[0][0]-0) + abs(permu[0][1]-0)) # (0,0)과 첫번째 사과간의 거리
    for i in range(N-1): #(N개의 사과들간의 거리를 구하는 for문)
        val += abs(permu[i][0] - permu[i+1][0]) + abs(permu[i][1]- permu[i+1][1])
    val += (abs(permu[N-1][0] - 0) + abs(permu[N-1][1] - 0)) # 마지막 사과와 (0,0)간의 거리
    if val < min_val: # 최종 이동거리가 min_val보다 작다면
        min_val = val # 그 값을 최소값으로 받아들임

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_val = float('inf') # 최소값을 구하기 위한 min_val, 가장 큰 수로 해줌
    for k in permutations(arr): # 사과들의 좌표를 순열로 모든 경우를 정리
        calc(k) # 순열로 정리한 사과들의 위치 좌표를 이동거리를 구하는 함수인 calc에 대입
    print(f'#{tc}',min_val) # 최소이동거리 출력






# # itertools 없이 재귀로 푼 경우
# import sys
# sys.stdin = open('rmv.txt')
# T = int(input())
#
# def dis(permu):
#     global min_val
#     val = 0
#     val += (abs(permu[0][0]-0) + abs(permu[0][1] - 0))
#     for i in range(N-1):
#         val += abs(permu[i][0] - permu[i+1][0]) + abs(permu[i][1]- permu[i+1][1])
#         if val>=min_val:
#             return
#     val += (abs(permu[N-1][0] - 0) + abs(permu[N-1][1] - 0))
#     if val < min_val:
#         min_val = val
#
# def calc(depth,arr):
#     if depth == N:
#         dis(path)
#         return
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             path.append(arr[i])
#             calc(depth+1, arr)
#             path.pop()
#             visited[i] = False
#
# for tc in range(1, 1 + T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     visited = [False]*N
#     path = []
#     min_val = float('inf')
#     calc(0,arr)
#     print(f'#{tc}',min_val)