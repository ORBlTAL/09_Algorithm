import sys
sys.stdin = open('input4.txt')

def find_min_cost(month, current_cost, a, b, c, d):
    global min_cost

    if current_cost >= min_cost: # 현재값이 이미 최소보다 크면 종료
        return
    if month > 11: # 달이 11보다 커지면 , 그 때의 최소값과 현재값일 비교해서 최소를 구함
        min_cost = min(min_cost, current_cost)
        return
    # 1일 이용권 선택
    # 현재 달의 이용일 수 * 1일권 가격을 더하고 다음달로 넘어감
    cost_d = a * arr[month]
    find_min_cost(month + 1, current_cost + cost_d, a, b, c, d)
    # 1달 이용권 선택. 1달권 가격을 더하고 다음달로 넘어감
    cost_m1 = b
    find_min_cost(month + 1, current_cost + cost_m1, a, b, c, d)
    # 3달 이용권 선택. 3달권 가격을 더하고 3달뒤로 넘어감
    cost_m3 = c
    find_min_cost(month + 3, current_cost + cost_m3, a, b, c, d)


T = int(input())
for tc in range(1 , 1 + T):
    a, b, c, d = map(int, input().split()) # 일, 달, 3달, 년 별 요금
    arr = list(map(int, input().split()))
    min_cost = d # 최소 비용을 1년 이용권 가격으로 초기화
    find_min_cost(0, 0, a, b, c, d)
    print(f'#{tc}', min_cost)