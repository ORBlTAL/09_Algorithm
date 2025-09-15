import sys
sys.stdin = open('input3.txt')
# # 순서는 동서남북
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]
#
# def count(list_a):
#     global cnt, new
#     if list_a not in new:
#         new.append(list_a[:])
#         cnt +=1
#
# def calc(cnt,i,j):
#     if cnt == 7:
#         count(path)
#         return
#     for k in range(4):
#         nr, nc = i + dr[k], j + dc[k]
#         if 0<=nr<4 and 0<=nc<4:
#             path.append(arr[nr][nc])
#             calc(cnt + 1, nr, nc)
#             path.pop()
#
# T = int(input())
# for tc in  range(1, 1 + T):
#     arr = [list(map(int, input().split()))for _ in range(4)]
#     path = []
#     new = []
#     cnt = 0
#     for i in range(4):
#         for j in range(4):
#             calc(0,i,j)
#     print(f'#{tc}',cnt)




# 델타 / 순서는 동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def count(list_a):
    global cnt, new # cnt, new를 글로벌로 선언
    key = tuple(list_a) # 불러온 path 리스트를 튜플로 변환
    if key not in new: # set new 안에 key가 없으면
        new.add(key) # key 추가
        cnt += 1 # 추가된 경우가 서로다른 일곱자리 수를 발견항 경우이므로 cnt +1 해줌

def calc(cnt, i, j):
    if cnt == 7:
        count(path) # 자리수가 7개일 때, 그때의 리스트를 count함수에 대입
        return
    for k in range(4):
        nr, nc = i + dr[k], j + dc[k] # 델타좌표
        if 0 <= nr < 4 and 0 <= nc < 4: # 인덱스 오류 방지
            path.append(arr[nr][nc]) # 해당 좌표값을 리스트에 추가
            calc(cnt + 1, nr, nc) # 재귀호출
            path.pop() # 넣은 값 pop으로 제거, 다음 델타 연산을 위해서

T = int(input())
for tc in range(1, 1 + T):
    arr = [list(map(int, input().split())) for _ in range(4)]
    new = set() # set로 선언해 중복을 방지
    cnt = 0 # 서로다른 일곱자리수 세는 변수 cnt

    for i in range(4): # 4x4 격자를 탐색하기 위한 이중for문
        for j in range(4):
            path = [arr[i][j]] # path 리스트 생성, 시작 좌표를 미리 넣어놔서 이동탐색횟수를 1번 줄임
            calc(1, i, j) # 시작 번호, 좌표를 함수에 대입

    print(f'#{tc}', cnt)
