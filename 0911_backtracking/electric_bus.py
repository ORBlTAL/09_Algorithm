import sys
sys.stdin = open('input3.txt')

def calc(station , battery, count): #
    global min_val
    if count > min_val:
        return
    # 종점 도달시, 인덱스 논리상 N - 1 번째가 종점 이므로 이와 같거나 클 때 최소 횟수를 구함
    if station >= N - 1:
        min_val = min(count, min_val) # 최소 충전횟수를 구하고 종료
        return
    # 다음정류장으로 넘어갈 때, 재귀로 함수에 다음 정류장 위치, 현재 배터리 -1, 카운트 증가
    calc(station + 1, new[station] -1 , count + 1)
    # 만약 배터리가 0보다 크다면 카운트를 안셈(배터리 교체없이도 가니까)
    if battery > 0:
        calc(station + 1, battery - 1, count)


T = int(input())
for tc in range(1, 1 + T):
    arr = list(map(int, input().split()))
    N = arr[0] # 정류장 개수
    new = arr[1:] # N-1개의 정류장 별 배터리 용량
    min_val = N # 최소의 초기 변수는 N으로
    calc(1, new[0]-1, 0)
    print(f'#{tc}',min_val)

