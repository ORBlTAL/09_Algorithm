#
# def check(row, col): # 가로 , 세로 , 대각선을 지움
#     # 1. 같은 열에 놓은 적이 있는가? 맨 처음 점음 (0,col), 여기서부터 현재 점까지
#     for i in range(row):
#         if visited[i][col]:
#             return False
#
#     # 2. 좌상단 대각선에 놓은 적이 있는가? (\) row, col 둘 중에 하나가 0일 될 때 까지 row -1 , col -1
#     i, j = row - 1, col - 1
#     while i >=0 and j >= 0: # 둘 중 하나라도 0이 될 때 까지 빼줌
#         if visited[i][j]:
#             return False
#         i -=1
#         j -=1
#
#     # # [참고] for문으로 하고 싶다!
#     # for i, j in zip(range(row - 1, -1 -1), range(col - 1, -1, -1)): # ????
#     #     if visited[i][j]:
#     #         return False
#
#     # 3. 우상단 대각선에 놓은 적이 있는가? (/) row는 감소, col은 증가
#     i, j = row -1, col + 1
#     while i>=0 and j < N: # 감소는 0 보다 크고, 증가는 N 보다 작고
#         if visited[i][j]:
#             return False
#         i -=1
#         j +=1
#
#     return True # False가 나온적이 없으면 True 반환
#
# # 종료 조건 : N개의 행을 모두 고려하면 종료
# # 가지의 수 : N 개의 열
# def recur(row):
#     global answer
#     if row == N:
#         # print(*path)
#         answer +=1
#         return
#     for col in range(N): # 1개의 행에 대해서 열들을 다 체크 => 반복문 써야함
#         # col을 선택했다.
#         # 가지치기 : 같은 열을 못 고르도록
#         # --> 유망하지 않은 케이스를 모두 삭제 (가로, 세로, 대각선)
#         if check(row, col) is False: # 유망하지 않은 것을 체크하는것. 이런거는 함수로 빼는게 편함
#             continue
#         visited[row][col] = 1
#         # path.append(col)
#         recur(row + 1)
#         # path.pop()
#         visited[row][col] = 0
#
# N = 4
# answer = 0 # 가능한 정답 수
# # path = [] # 임시변수 (경로 출력을 위해)
# visited = [[0] * N for _ in range(N)] # 가로 세로 대각선을 고려해야 하므로 2차원
# recur(0)
# print(f'N = {N}, answer = {answer}')
#
# N = 8
# answer = 0 # 가능한 정답 수
# # path = [] # 임시변수 (경로 출력을 위해)
# visited = [[0] * N for _ in range(N)] # 가로 세로 대각선을 고려해야 하므로 2차원
# recur(0)
# print(f'N = {N}, answer = {answer}')





def check(row, col): # 가로 , 세로 , 대각선을 지움
    # 1. 같은 열에 놓은 적이 있는가? 맨 처음 점음 (0,col), 여기서부터 현재 점까지
    for i in range(row):
        if visited[i][col]:
            return False

    # 2. 좌상단 대각선에 놓은 적이 있는가? (\) row, col 둘 중에 하나가 0일 될 때 까지 row -1 , col -1
    i, j = row - 1, col - 1
    while i >=0 and j >= 0: # 둘 중 하나라도 0이 될 때 까지 빼줌
        if visited[i][j]:
            return False
        i -=1
        j -=1

    # # [참고] for문으로 하고 싶다!
    # for i, j in zip(range(row - 1, -1 -1), range(col - 1, -1, -1)): # ????
    #     if visited[i][j]:
    #         return False

    # 3. 우상단 대각선에 놓은 적이 있는가? (/) row는 감소, col은 증가
    i, j = row -1, col + 1
    while i>=0 and j < N: # 감소는 0 보다 크고, 증가는 N 보다 작고
        if visited[i][j]:
            return False
        i -=1
        j +=1

    return True # False가 나온적이 없으면 True 반환

# 종료 조건 : N개의 행을 모두 고려하면 종료
# 가지의 수 : N 개의 열
def recur(row):
    global answer
    if row == N:
        # print(*path)
        answer +=1
        return
    for col in range(N): # 1개의 행에 대해서 열들을 다 체크 => 반복문 써야함
        # col을 선택했다.
        # 가지치기 : 같은 열을 못 고르도록
        # --> 유망하지 않은 케이스를 모두 삭제 (가로, 세로, 대각선)
        if check(row, col) is False: # 유망하지 않은 것을 체크하는것. 이런거는 함수로 빼는게 편함
            continue
        visited[row][col] = 1
        # path.append(col)
        recur(row + 1)
        # path.pop()
        visited[row][col] = 0

N = 4
answer = 0 # 가능한 정답 수
# path = [] # 임시변수 (경로 출력을 위해)
visited = [[0] * N for _ in range(N)] # 가로 세로 대각선을 고려해야 하므로 2차원
recur(0)
print(f'N = {N}, answer = {answer}')

N = 8
answer = 0 # 가능한 정답 수
# path = [] # 임시변수 (경로 출력을 위해)
visited = [[0] * N for _ in range(N)] # 가로 세로 대각선을 고려해야 하므로 2차원
recur(0)
print(f'N = {N}, answer = {answer}')