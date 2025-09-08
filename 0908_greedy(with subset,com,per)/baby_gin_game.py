# import sys
# from itertools import combinations
# sys.stdin = open('input3.txt')
# T = int(input())
#
# def is_run(card):
#     return card[0] + 2 == card[1] + 1 == card[2] # run 조건이 참일 때 리턴
#
# def triplet(card):
#     return card[0] == card[1] == card[2] # triplet 조건이 참일 때 리턴
#
# def baby_gin_comb(card):
#     for group in combinations(range(6),3): # 6개 중에서 3개를 뽑아 조합으로
#         g1 = []
#         for idx in group: # 위에서 뽑은 조합 요소를 토대로 g1 리스트에 3개씩 저장
#             g1.append(card[idx])
#
#         g2 = []
#         for i in range(6): # 위의 그룹에 속하지 않는 카드들끼리 뽑아서 g2 리스트에 저장
#             if i not in group:
#                 g2.append(card[i])
#
#         ok1 = is_run(g1) or triplet(g1) # g1이 run 또는 triplet일 떄
#         ok2 = is_run(g2) or triplet(g2) # g2가 run 또는 tripelt 일 때
#         if ok1 or ok2: # 둘 다 둘 중 하나는 충족하고 있어야 만족한다.
#             return True
#     return False
#
# for tc in range(1 , 1 + T):
#     arr = list(map(int, input().split()))
#     player_1 = []
#     player_2 = []
#     for i in range(len(arr)):
#         if i % 2 == 0:
#             player_1.append(arr[i])
#         else:
#             player_2.append(arr[i])
#     player_1.sort()
#     player_2.sort()
#
#     if (baby_gin_comb(player_1) and baby_gin_comb(player_2)) or baby_gin_comb(player_1):
#         print(f'#{tc}',1)
#     elif baby_gin_comb(player_2):
#         print(f'#{tc}',2)
#     else:
#         print(f'#{tc}',0)
#
#




import sys
sys.stdin = open('input3.txt')
T = int(input())

def check_win(counts):
    # triplet: 같은 숫자 3장 이상
    for d in range(10):
        if counts[d] >= 3:
            return True
    # run: i, i+1, i+2 각각 1장 이상
    for i in range(8):
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            return True
    return False

# run 과 triplet 확인하는 함수
def is_run(card):
    return card[0] + 2 == card[1] + 1 == card[2]

def triplet(card):
    return card[0] == card[1] == card[2]

for tc in range(1 , 1 + T):
    arr = list(map(int, input().split()))
    # 각 플레이어의 보유 카운트
    p1 = [0] * 10
    p2 = [0] * 10
    winner = 0

    for i in range(12):
        card = arr[i]
        if i % 2 == 0:
            # 플레이어 1 차례
            p1[card] += 1 # 뽑은 카드의 인덱스의 값을 증가시킴 -> 차후 triplet 판단
            # 먼저 run, triplet 채운 되는 사람이 승자이니 p1이 승리인지 아닌지 판단
            if i >= 4:
                if check_win(p1):
                    winner = 1
                    break
        else:
            # 플레이어 2 차례
            p2[card] += 1
            if i >= 5:
                if check_win(p2):
                    winner = 2
                    break

    print(f'#{tc} {winner}')

#
#
#
#
#
#
#
# # def triple(arr):
# #     i = 0
# #     while i < 10:
# #         cnt = 0
# #         for j in range(6):
# #             if arr[j] == i:
# #                 cnt+=1
# #         if cnt ==3:
# #             return True
# #         i +=1
# #
# # def run(arr):
# #     for i in range(4):
# #         if arr[i]+2 == arr[i+1] + 1 == arr[i+2]:
# #             return True
