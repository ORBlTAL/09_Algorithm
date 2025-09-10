import sys
sys.stdin = open('input4.txt')
T = int(input())
def binary_search(arr, target):
    left, right = 0 , len(arr) - 1
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return -1

for tc in range(1, 1 + T):
    N, M = map(int ,input().split())
    arr_N = list(map(int, input().split()))
    arr_M = list(map(int, input().split()))

    k = binary_search(arr_N, arr_M[0])
    print(k)