"""
b 가 a 보다 크고, c가 b 보다 크면 조건 만족이니 0을 출력
c 가 3보다 작으면 애초에 성립이 불가이니 -1 출력
a 가 b보다 크면 두 수의 차 + 1 만큼 사탕을 먹어야 함 / b 가 c보다 커도 마찬가지
이 떄 중요한건 b 에서 c 보다 작게끔 수를 뺀 뒤에 a 와 b의 관계 고려 이다. 연산 후에도 a가 b보다 작으면 상관 없지만,
a가 b보다 크거나 같게 되면 그 부분도 고려해 주어야 한다.
"""
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, 1 + T):
    a, b, c = map(int, input().split())
    # 불가능 조건 : b < 2 이거나 c < 3 이면 불가
    if b < 2 or c < 3:
        print(f'#{tc}', -1)
        continue
    # 이 경우에는 조건을 충족하므로 0을 출력
    if (a < b < c):
        print(f'#{tc}', 0)
        continue

    # b가 c보다 크거나 같은 경우 ,
    if b >= c:
        b_new = c - 1 # b_new는 c-1 이어야 조건 충족
    else:
        b_new = b # 아니면 그대로 유지

    if a >= b_new: # b,c 간의 연산을 마친 b_new로 a를 판단해야함
        a_new = b_new - 1 # a가 b_new와 같거나 크면 a_new 는 b_new - 1 이어야함
    else:
        a_new = a # 아니면 그대로 유지

    result = (a - a_new) + (b - b_new) # 원본과 원본에서 줄인 값의 차이들을 합하면 먹어야 할 사탕개수 도출 가능
    print(f'#{tc}',result)




# import sys
# sys.stdin = open('rmv.txt')
# T = int(input())
# for tc in range(1, 1 + T):
#     a, b, c = map(int, input().split())
#     # 불가능 조건 : b < 2 이거나 c < 3 이면 불가
#     if b < 2 or c < 3:
#         print(f'#{tc}', -1)
#         continue
#     # 이 경우에는 조건을 충족하므로 0을 출력
#     if (a < b < c):
#         print(f'#{tc}', 0)
#         continue
#     # b >= c 일 때 b_new를 c-1로 선언 , 아니면 b 유지
#     b_new = c - 1 if b >= c else b
#     # a >= b_new 일 때 a new를 b_new -1로 선언, 아니면 a 유지
#     a_new = b_new -1 if a >= b_new else a
#
#     result = (a - a_new) + (b - b_new) # 원본과 원본에서 줄인 값의 차이들을 합하면 먹어야 할 사탕개수 도출 가능
#     print(f'#{tc}',result)