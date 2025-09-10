import sys
sys.stdin = open('input2.txt')
T = int(input())

def merge(left, right):
    global cnt # 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우를 세는 cnt를 글로벌 변수로 불러옴
    result = [0] * (len(left) + len(right)) # 병합할 리스트의 길이 지정
    l = r = 0
    if left[-1] > right[-1]: # 왼쪽 마지막 원소가 오른쪽 보다 클 경우
        cnt +=1 # cnt 증가

    while l < len(left) and r < len(right): # 받아온 리스트의 길이 전체를 다 반영
        if left[l] < right[r]: # 왼쪽 요소가 우측보다 작으면
            result[l+r] = left[l] # 왼쪽 요소를 리스트에 할당
            l += 1 # 왼쪽 인덱스 +1
        else:
            result[l+r] = right[r] # 우측 요소가 좌측보다 작을때는 반대로 우측 요소를 리스트에 할당
            r += 1 # 우측 인덱스 +1

    while l < len(left): # 좌측 남은거 넣어주기
        result[l+r] = left[l]
        l +=1
    while r < len(right):
        result[l+r] = right[r] # 우측 남은거 넣어주기
        r +=1

    return result


def merge_sort(arr):
    if len(arr) <= 1: # 길이가 1일 될 때 까지 나눔
        return arr # 1이 되면 반환
    mid = len(arr) // 2 # 중간 인덱스 구하기
    left_half = arr[:mid] # 기존 리스트의 좌측
    right_half = arr[mid:] # 기존 리스트의 우측

    left_sorted = merge_sort(left_half) # 왼쪽 부분을 다시 왼쪽, 오른쪽으로 나눔(1이될 때 까지)
    right_sorted = merge_sort(right_half) # 우측 부분을 다시 왼쪽, 오른쪽으로 나눔(1이될 때 까지)

    return merge(left_sorted, right_sorted) # 왼쪽 부분 쪼갠것과 우측 쪼갠것을 병합.


for tc in range(1, 1 + T):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    sorted_array = merge_sort(arr)
    # print(sorted_array)
    print(f'#{tc}', sorted_array[len(sorted_array)//2], cnt) # 정렬된 리스트의 중간값과 cnt 출력