import sys
sys.stdin = open('input_ct_4.txt')
n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r)-1, int(c)-1

select = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}
dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]

dir_v = select[d]

for _ in range(t):
    nr, nc = r + dr[dir_v] , c + dc[dir_v]
    if 0<=nr<n and 0<=nc<n:
        r,c = nr, nc
    else:
        dir_v = 3 - dir_v
print(r+1, c+1)



























# n, t = tuple(map(int, input().split()))
# x, y, c_dir = tuple(input().split())
#
# # 각 알파벳 별 방향 번호를 설정합니다.
# mapper = {
#     'R': 0,
#     'D': 1,
#     'U': 2,
#     'L': 3
# }
# x, y, move_dir = int(x) - 1, int(y) - 1, mapper[c_dir]
#
# dxs = [0, 1, -1,  0]
# dys = [1, 0,  0, -1]
#
#
# def in_range(x, y):
#     return 0 <= x < n and 0 <= y < n
#
#
# # simulation 진행
# for _ in range(t):
#     nx, ny = x + dxs[move_dir], y + dys[move_dir]
#     # 범위 안에 들어온다면 그대로 진행합니다.
#     if in_range(nx, ny):
#         x, y = nx, ny
#     # 벽에 부딪힌다면, 방향을 바꿔줍니다.
#     else:
#         move_dir = 3 - move_dir
#
# print(x + 1, y + 1)
