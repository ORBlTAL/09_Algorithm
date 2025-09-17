"""
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
"""

import sys
sys.stdin = open('nd.txt')
T = int(input())
for tc in range(1, 1 + T):
    V , E = map(int,input().split())
