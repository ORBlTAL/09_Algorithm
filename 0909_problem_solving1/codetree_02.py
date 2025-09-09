"""
L 이면 좌로 90도 회전, R 이면 우로 90도 회전인데
"""
import sys
sys.stdin = open('input_ct_2.txt')
coordinate = str(input())
# 상우하좌
dir = [(0,1),(1,0),(0,-1),(-1,0)]
sp = 0
x , y = 0, 0
for i in coordinate:
    if i == 'L':
        sp = (sp - 1) % 4
    elif i == 'R':
        sp = (sp + 1) % 4
    elif i == 'F':
        dx , dy = dir[sp]
        x += dx
        y += dy
print(x,y)



