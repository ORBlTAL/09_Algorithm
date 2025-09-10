# 이진탐색 방법 1 : while로 구현
def binary_search_while(target):
    left = 0             # 검색 시작점
    right = len(arr) - 1 # 검색 끝점
    cnt = 0

    while left <= right: # 교차되면 못 찾은 것
        mid = (left + right) // 2
        cnt +=1 # 검색횟수 추가

        if arr[mid] == target:
            return mid, cnt # mid 위치에 존재한다고 return

        # target 보다 정답이 왼쪽에 있는 경우
        if target < arr[mid]:
            right = mid - 1
        # tatget 보다 정답이 오른쪽에 있는 경우
        else:
            left = mid + 1
    # 못찾은 경우 -1을 출력
    return -1, cnt

#  이진탐색 방법 2 : 재귀함수 호출
def binary_search_recur(left, right, target):

    if left > right:
        return -1
    mid = (left+right) // 2
    if target == arr[mid]:
        return mid

    if target < arr[mid]:
        return binary_search_recur(left, mid - 1, target)
    else:
        return binary_search_recur(mid + 1, right, target)


arr = [4, 2, 9, 7, 11, 23, 19]
# 이진 검색은 항상 정렬된 데이터에 적용
# 병합, 퀵정렬로 정렬을 해야함

arr.sort() # 2 4 7 9 11 19 23

# binary_search_while(0, len(arr) -1) # 처음과 끝을 전달
print(f'9 = {binary_search_while(9)}번째에 위치')