"""
점원들중에 아무나 선택하면 되므로 조합을 이용해 풀이
조합의 경우 1 부터 N 까지 모든 경우를 다 살펴봄
각 경우에서의 합을 B보다 크거나 같은지 판단하고, 그럴경우 합과 B의 차 들 중에서 최소를 구하고 출력한다.
"""
import sys
from itertools import combinations
sys.stdin = open('input2.txt')
T = int(input())
for tc in range(1, 1 + T):
    N, B = map(int,input().split())
    arr = list(map(int,input().split()))

    min_val = float('inf')
    for i in range(1, N + 1): # 범위는 1부터 N까지
        for k in combinations(arr, i): # 조합을 받아온 키 정보를 토대로 구함
            print(k)
            current = sum(k) # 각 조합의 합을 current에 저장

            if current >= B: # B보다 크 거나 같은 경우에만
                min_val = min(min_val, current - B) # current - B와 최소를 비교해 최소를 구함
    # print(f'#{tc}', min_val)

