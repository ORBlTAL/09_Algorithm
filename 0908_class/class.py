# # 3명의 친구 부분집합 찾기
# arr = ['O', 'X']
# name = ['MIN' , 'CO', 'TIM']
# path = []
#
# def recur(cnt):
#     # 종료조건(3명을 모두 고려할 때 까지)
#     if cnt == 3: # 한명을 고려할 때 마다 cnt가 올라가야 하므로, cnt를 재귀로 받음
#         print(*path)
#         return
#     # 재귀호출 후보군
#     # - 부분집합에 포함되는 경우 (O를 추가)
#     path.append(arr[0])
#     recur(cnt + 1)
#     path.pop()
#
#     # - 포함되지 않는 경우 (X를 추가)
#     path.append(arr[1])
#     recur(cnt+1)
#     path.pop()
#
#
# recur(0) # 0명을 고려한 상태로 시작





# # 궅이 append , pop 으로 해야할 까? 실전용
# """
# 두 번쨰 선택에서는 'MIN' 이라는 친구가 포함된 상태를 저장하면서
# """
# name = ['MIN' , 'CO', 'TIM']
#
# def recur(cnt, subset):
#     if cnt == 3:
#         print(*subset)
#         return
#
#     # 부분집합에 포함 시키는 경우
#     recur(cnt+1, subset + [name[cnt]])
#
#     # 포함 시키지 않는 경우
#     recur(cnt + 1, subset)
#
# recur(0, []) # 시작은 path에 아무도 없으므로 빈 상태로





# # 바이너리 카운팅
# arr = [1,2,3,4]
#
# # 부분 집합
# # i: 0~2^n == i번째 부분집합
# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         if i & (1 << idx):
#             print(arr[idx], end = ' ')
#     print()
#
#
# # 부분 집합의 함수로 구현
# n = len(arr)
# def get_sub(tar):
#     for i in range(n):
#         if tar & 0x1:
#             print(arr[i], end=' ')
#         tar >>=1
#
# for target in range(1 << n):
#     get_sub(target)
#     print()





# 조합 / 5명 중 3명을 순서없이 고르기
arr = ['A' , 'B' , 'C', 'D','E']
N = 3
path = []

def recur(cnt, start):
    # 0명부터 시작해 N명을 뽑으면 종료
    if cnt == N:
        print(*path)
        return

    for i in range(start, len(arr)): # start가 없으면 중복조합이 된다.
        path.append(arr[i])
        recur(cnt + 1, i + 1) # i번째를 골랐으니, 다음 선택은 i + 1 부터 고려(중복허용, i + 1을 넣을시 중복 허용 x
        path.pop()

recur(0,0)




# """
# [문제] 동전의 최소 개수
# 규칙: 큰 동전부터 나누자
#
# Greedy 문제의 단골 손님 : sort() -> 정렬(오름, 내림)을 해줘야 할 때가 많음
# 정렬 연습 : 튜플이라면? 인스턴스 리스트? 역순이라면?
# listed.sort() vs sorted()
# """
# coin_list = [100, 50, 500, 10]
# target = 1730
# result = 0
# coin_list.sort(reverse=True)
#
# for coin in coin_list:
#     possible_cnt = target // coin # 현재 동전으로 가능한 최대 수
#     result += possible_cnt # 정답에 더해준다
#     target -= coin * possible_cnt # 금액을 빼준다.
# print(result)





"""
화장실 문제
많은 사람이 덜 기다릴수록 최소가 된다.
시간이 적은사람부터 들어가면 사람들이 기다리는 시간의 누적이 최소가 된다.
ㄴ> 입력받은 데이터를 먼저 정렬해야함.
"""