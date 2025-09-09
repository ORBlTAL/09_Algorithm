import sys
sys.stdin = open('input_ct_1.txt')
# dir = []
# for move in moves:
#     dir.append(move[0])
# print(dir)

n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]
x , y = 0, 0
for i in moves:
    if i[0] == 'N':
        y += int(i[1])
    elif i[0] == 'E':
        x += int(i[1])
    elif i[0] == 'W':
        x -= int(i[1])
    elif i[0] == 'S':
        y -= int(i[1])
print(f'{x} {y}')