# 1. 분할
# 2. 정복 & 병합(정렬)

"""
좌측과 우측의 쪼개긴 값들을 받아와서 오름차순으로 병합해야함.일단 얘네들을 담을 리스트와, 비교할 인덱스가 필요
while문을 통해 좌측, 우측 리스트에 비교할 대상이 있을 때까지 반복. 리스트의 길이로 판단. 인덱스도 업데이트 필요
남아있는 데이터를 추가하는 과정도 필요.
"""
def merge(left, right):
    # 두 리스트를 병합한 결과
    result = [0] * (len(left) + len(right))
    l = r = 0 # 인덱스

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 왼쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    # 오른쪽 리스트에 남은 데이터들을 모두 result 에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result

"""
길이가 1일 될 때 까지 쪼개야함. 길이가 1이 되면 return해서 끝냄
절반씩 나누는것은 리스트 슬라이싱 이용 : mid 는 입력받은 배열 길이의 절반, 이걸 토대로 좌측, 우측 나눔
좌측, 우측으로 나눈 리스트를 길이가 1일 될 때 까지 나눠야 하므로 여기서 재귀호출 이용
재귀로 길이가 다 쪼개낀 리스트들을 오름차순으로 병합해야 하므로 merge 함수를 이용해 새 리스트에 합쳐서 출력
"""
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    # 절반 씩 분할하여 출력해라 (재귀호출 전에 반씩 쪼개는 작업)
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    # print(left,right)

    # 길이가 1일 될 때 까지, 필요시 더 호출해서 쪼개야함(재귀호출 필요)
    left_list = merge_sort(left)
    right_list = merge_sort(right)

    # 재귀호출 후 돌와았을때 필요한 작업을 재귀 호출 밑에 적음
    # 쪼개기만 하고, 순서대로 나열을 안했으니 그걸 여기서 해야함.(병합하면서 오름차순 정리 구현 필요)
    merge_list = merge(left_list, right_list)
    return merge_list

arr= [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)