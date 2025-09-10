import sys
sys.stdin = open('input3.txt')
T = int(input())

def partition(arr, start,end):
    pivot = arr[end] # 초기 피벗은 리스트의 맨 우측 값으로
    i = start - 1 # 작은 원소 인덱스
    for j in range(start,end): # 리스트 순회
        if arr[j] < pivot: # 현재 값이 피벗보다 작으면
            i +=1 # 작은 원소 인덱스를 우측으로 한칸 이동
            arr[j],arr[i] = arr[i],arr[j] # i와 j 번째 인덱스의 값을 바꿈
    arr[i+1],arr[end] =  arr[end], arr[i+1] # 최종적으로 i + 1 번째와 마지막(피벗 지정된 곳) 을 바꿔줌

    return i + 1 # 피벗이 저장된 곳의 좌표를 반환

def quick_sort(arr, start, end):
    # 정렬 범위에 원소가 1개 이하일 때
    if start < end:
        # 피벗의 인덱스 위치를 계산하는 partition 함수 호출
        pivot_idx = partition(arr, start,end)
        # 피벗을 기준으로 나뉜 왼쪽 부분을 재귀적으로 정렬
        quick_sort(arr, start, pivot_idx-1)
        # 피벗을 지준으로 나뉜 우측 부분을 재귀적으로 정렬
        quick_sort(arr, pivot_idx+1 , end)


for tc in range(1, 1 + T):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N-1)
    print(f'#{tc}',arr[N//2])