import sys
from itertools import permutations
sys.stdin = open('input2.txt')

def make(arr, a ,N, min_val):

    for k in permutations(a):
        sum_val = 0
        for i in range(N):
            sum_val += arr[i][k[i]]
            if sum_val > min_val:
                break
        else:
            min_val = min(sum_val,min_val)
    return min_val

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    min_val = float('inf')
    a = list(range(N))
    print(f'#{tc}',make(arr,a,N,min_val))