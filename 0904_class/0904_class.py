# for i in range(1,4):
#     for j in range(1,4):
#         for k in range(1,4):
#             for l in range(1,4):
#                 print(i,j,k,l)

# path = []
# N = 3
# def run(lev):
#     if lev == N:
#         print(path)
#         return
#     for i in range(1,4):
#         path.append(i)
#         run(lev + 1)
#         path.pop()
# run(0)


# def kfc(n):
#     if n == 3: # 종료조건
#         return
#     print(n, end = ' ')
#     kfc(n + 1) # 재귀
#     kfc(n + 1)
#     print(n, end = ' ') # 재귀 함수가 끝나고 나서 출력되는 부분
# kfc(0) # 시작점 : 0


# def kfc(x):
#     if x == 2:
#         return
#     kfc(x + 1)
#     kfc(x + 1)
#     print(x)
# kfc(0)


# """
# 중복순열
# [0,1,2] 3개의 카드가 존재 -> 2개를 뽑는다.
# """
# path = [] # used, visited... --> 뽑은 카드들을 저장
#
# # 기저조건(종료조건) : 2개의 가트를 모두 뽑았다면 종료
# #  - 시작점 : 0갱의 카드를 고른 상태부터 시작
# # 다른 재귀호출 구조 : [0, 1, 2] 카드 중 하나를 고른다.
# def recur(cnt):
#     if cnt == 2: # 0부터 시작해서 2개를 뽑았다. 그럼 종료
#         print(*path)
#         return
#     # 카드 0, 1, 2 중 하나를 선택
#     for num in range(3):
#         path.append(num)
#         recur(cnt + 1)
#         path.pop()
#
#     # path.append(0)
#     # recur(cnt + 1)  # 하나 선택했으니 다음 선택으로 이동
#     # path.pop() # 쌓이게 되는걸 없에줘야 한다.
#     #
#     # path.append(1)
#     # recur(cnt + 1)
#     # path.pop()
#     #
#     # path.append(2)
#     # recur(cnt + 1)
#     # path.pop()
#
# recur(0)



# # 1부터 7까지 3장씩 뽑는 중복 순열
# path = []
# def recur(cnt):
#     if cnt == 3:
#         print(*path)
#         return
#
#     for num in range(1,7):
#         path.append(num)
#         recur(cnt + 1)
#         path.pop()
#
# recur(0)



# # 순열 비효율 버전
#
# path = []
# def recur(cnt):
#     if cnt == 3:
#         print(*path)
#         return
#
#     for num in range(1,7):
#         # if num not in path:
#         #in을 쓰면 리스트 전부를 다 확인하니 느림
#         if num in path: # 이미 path에 있는 숫자는 생략 -> 근데 이 방식이 모두 조사하니 매우 느려짐
#             continue
#         path.append(num)
#         recur(cnt + 1)
#         path.pop()
#
# recur(0)



# # 순열 효율 버전
#
# path = []
# # used = [False, False, False, False, False, False, False] # 골라야 하는 수 만큼 만들어 준다.
# # used [False] * N # N개의 카드 종류가 있는 경우
# used = [False] * 7 # 1~6까지의 카드 숫자 사용여부를 기록(0은 버린다)
#
# def recur(cnt):
#     if cnt == 3:
#         print(*path)
#         return
#
#     for num in range(1,7):
#         if used[num]: # 중복 제거
#             continue
#         used[num] = 1 # 기록표시
#         path.append(num)
#         recur(cnt + 1)
#         path.pop()
#         used[num] = 0 # 기록 초기화
#
# recur(0)


# """
# 완전탐색 문제 1. 주사위 눈의 합
#  - 3개의 주사위를 던져 나올 수 있는 중복 순열에 대해, 합이 10이하가 나오는 경우는 총 몇가지 인가?
# """
# path = [] # 무조건 기존 주사위를 기록해놔야 할까 ...??
# result = 0
# def recur(cnt):
#     global result
#     if cnt == 3:
#         # print(*path)
#         if sum(path) <=10:
#             print(*path)
#             result +=1
#         return
#     for num in range(1,7):
#         path.append(num)
#         recur(cnt + 1)
#         path.pop()
# recur(0)
# print(result)
#
# """
# 위에서 최적화 할 수 있는 방법 2가지
#     1. 만약에 첫 주사위가 6, 두번째가 4면 3번째를 볼 필요가 없음. 이걸 가지치가함
#     2. append 해서 path를 반드시 기록을 해야할까?(이건 교육을 위해서 보는거지 실제로는 없어도 됨)
# """
# 누적합을 활용하는 버전
result = 0
def recur(cnt, total): # 합을 파라미터로 만든다.
    global result
    # 최적화 1번 : 기저 조건에서 많은 경우의 수들을 줄일 수 있다.
    if total > 10:
        return

    if cnt == 3:
        # print(*path)
        # if total <=10:
        #     result +=1
        result +=1
        return
    for num in range(1,7):
        # total +=num
        # recur(cnt + 1)
        # total -=num
        recur(cnt + 1, total + num)
recur(0, 0)
print(result)

"""
문제2
A , J, Q, K 네 종류의 카드들이 충분히 있음
이 중 , 5장의 카드를 뽑아 나열하는데 같은 종류의 카드가 세 장 연속으로 나오는 경우의 수.
"""
cards = ['A','J','Q','K']
path = []
result = 0

# 연속된 3개의 같은 카드가 나오면 return True, 아니면 False
def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False

def recur(cnt):
    global result
    if cnt == 5:
        # Todo: 연속된 3개가 나오면 counting -> 함수로 만들어서 빼기
        if count_three():
            result += 1
            print(*path)
        return
    # 4개의 카드 중 하나를 선택
    for idx in range(len(cards)):
        path.append(cards[idx])
        recur(cnt + 1)
        path.pop()
recur(0)
print(result)






