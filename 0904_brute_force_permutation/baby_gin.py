# import sys
# sys.stdin = open('input.txt')
#
# path = []
# def triplet(path):
#     for i in range(4):
#         if path[i] == path[i + 1] == path[i + 2]:
#             return True
#
#
# def run(path):
#     for i in range(4):
#         if path[i] + 2 == path[i + 1] + 1 == path[i + 2]:
#             return True
#
#
# def gin(x,num):
#     if x == 6:
#         if triplet(path) and run(path):
#             if num in ''.join(map(str,path)):
#                 print(1)
#         return
#     for i in range(0, 10):
#         path.append(i)
#         gin(x + 1,num)
#         path.pop()
#
# T = int(input())
# for tc in range(1, 1 + T):
#     num = input()
#     gin(0,num)


import sys
sys.stdin = open('input.txt')
def is_triplet(arr): # 트리플렛 판별 코드
    return arr[0] == arr[1] == arr[2]

def is_run(arr): # run 판별 코드
    return arr[0] + 2 == arr[1] + 1 == arr[2]

def check_babygin(num):
    for i in range(1 << 6):
        group1, group2 = [], []
        for j in range(6):
            if i & (1 << j):
                group1.append(num[j])
            else:
                group2.append(num[j])
        if len(group1) == 3 and len(group2) == 3:
            group1.sort()
            group2.sort()
            if (is_triplet(group1) or is_run(group1)) and (is_triplet(group2) or is_run(group2)):
                return 1
    return 0

T = int(input())
for tc in range(1, 1+T):
    num = list(map(int, input()))
    print(f'#{tc}',check_babygin(num))
