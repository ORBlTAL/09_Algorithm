import sys
sys.stdin = open('input.txt')
T = int(input())
def partition(arr, start,end):
    pivot = arr[end] # 피벗 설정. 가장 오른쪽 인덱스로
    i = start - 1 # 피벗보다 작은 원소들을 저장할 인덱스

    for j in range(start,end): # 배열 순회
        if arr[j] < pivot: # 해당 배열의 원소가 피벗보다 작을 시
            i+=1 # 작은 원소 그룹의 경계를 한 칸 오른쪽으로 이동
            arr[i],arr[j] = arr[j],arr[i] # 현재 원소와 i 번째 원소의 위치를 교환해 작은 것을 왼쪽으로 보냄

    arr[i+1], arr[end] = arr[end] , arr[i+1] # for문을 다 마치고 피벗과 i+1 번째 위치의 원소와 교환

    return i + 1 # 피벗의 최종 위치를 인덱스로 반환

def quick_sort(arr, start, end):
    if start < end: # 정렬 범위에 원소가 1개 이하일 때
        pivot_idx = partition(arr, start, end) # 피벗으로 지정할 인덱스 구하기

        quick_sort(arr,start, pivot_idx-1) # 피벗 기준으로 나뉜 왼쪽부분을 재귀적으로 정리
        quick_sort(arr,pivot_idx+1,end) # 피벗 기준으로 나뉜 오른쪽 부분을 재귀적으로 정리


for tc in range(1, 1 + T):
    arr = list(map(int, input().split()))
    quick_sort(arr, 0 , len(arr)-1)
    print(f'#{tc}',*arr)