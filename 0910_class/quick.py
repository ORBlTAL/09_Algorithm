# quick with lomuto

# arr , left, right 여기서 left, right는 인덱스로 첫 시작에는 각각 처음과 끝을 표시
# 데이터가 하나만 남게 되면 left랑 right랑 똑같아짐 => 이때까지 계속 쪼개면서 진행
def partition(arr, start, end):
    """
    분할(partition)을 담당하는 함수
    - 가장 오른쪽 원소(arr[end])를 피벗으로 설정
    - 피벗보다 작은 값들은 왼쪽으로, 큰 값들은 오른쪽으로 재배치
    - 최종적으로 피벗이 있어야 할 올바른 위치의 인덱스를 반환
    """
    # 피벗을 가장 오른쪽 원소로 설정
    pivot = arr[end]
    # 피벗보다 작은 원소들을 저장할 경계 인덱스 i
    i = start - 1

    # start 부터 end-1까지 순회
    for j in range(start, end):
        # 현재 원소가 피벗보다 작으면,
        if arr[j] < pivot:
            # 작은 원소 그룹의 경계를 한 칸 오른쪽으로 이동
            i +=1
            # 경계(i)와 현재 원소(j)의 위치를 교환하여, 작은 원소를 왼쪽으로 보냄
            arr[i],arr[j] = arr[j],arr[i]
    # 모든 순회가 끝나면, i+1 위치가 피벗이 들어갈 자리
    # 피벗(arr[end])과 경계 다음 위치(arr[i+1])의 값을 교환
    arr[i+1],arr[end] = arr[end],arr[i+1]
    # 피벗의 최종 위치 인덱스를 반환
    return i+1


def quick_sort(arr , start, end):
    if start < end:
        pivot_idx = partition(arr, start, end)

        quick_sort(arr, start, pivot_idx-1)
        quick_sort(arr, pivot_idx+1, end)


data_list = [3, 2, 4, 6, 9, 1, 8, 7, 5]
print(f'정렬 전 : {data_list}')

quick_sort(data_list, 0, len(data_list) - 1)
print(f'정렬 후 : {data_list}')