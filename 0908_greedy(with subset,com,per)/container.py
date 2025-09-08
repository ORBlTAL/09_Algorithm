"""
컨테이너 무게랑 트럭 용량을 역순으로 정리한다음, 서로 매칭 시켜서 가능한 경우 그 값을 더함
"""
import sys
sys.stdin = open('input.txt')
T = int(input())

def calc(weight, capacity,a):
    global k
    # 종료 조건 : 컨테이너 무게, 트럭을 더 조회할 게 없으면 종료
    if a >=len(weight) or a >= len(capacity):
        return k
    # 화물 무게 조회
    for i in range(a,len(weight)):
        # 컨테이너 용량 조회
        for j in range(a,len(capacity)):
            if weight[i] <= capacity[j]: # 무게보다 컨테이너가 크거나 같을경우만 실을 수 있으므로
                k+=weight[i] # 그때의 무게값을 더함
                weight[a], weight[i] = weight[i], weight[a] # 배정된 값을 앞으로 스왑해 다음 재귀에서 안쓰이도록 함
                capacity[a], capacity[i] = capacity[i], capacity[a]
                return calc(weight, capacity, a + 1) # 재귀 호출로 다음 범위 계산
    # 남은 트럭들 중 어느 것도 매칭이 안 되면 종료
    return k

for tc in range(1 , 1 + T):
    N , M = map(int, input().split())
    weight = list(map(int,input().split()))
    capacity = list(map(int, input().split()))
    # 무게 , 용량 매칭시키기 편하게 내림차순으로 정렬
    weight.sort(reverse=True)
    capacity.sort(reverse=True)
    k = 0
    a = 0
    result = calc(weight, capacity, a)
    print(f'#{tc}',result)




