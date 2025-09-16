import sys
sys.stdin = open('input.txt')   # 입력을 파일에서 읽어오도록 설정
from heapq import heappush, heappop

def prim(start_node):
    # 우선순위 큐 (가중치, 노드) 형태
    pq = [(0, start_node)]

    # MST 배열: 해당 노드가 최소 신장 트리에 포함되었는지 여부 (0=미방문, 1=방문)
    MST = [0] * (V+1)

    # 최소 비용 합산 변수
    min_weight = 0

    # 우선순위 큐가 빌 때까지 반복
    while pq:
        weight, node = heappop(pq)  # 현재 가중치가 가장 작은 간선 선택

        # 이미 방문한 노드면 스킵
        if MST[node]:
            continue

        # 방문 처리 및 가중치 누적
        MST[node] = 1
        min_weight += weight

        # 현재 노드와 연결된 다른 노드 탐색
        for next_node in range(V+1):
            # 간선이 없으면 스킵
            if graph[node][next_node] == 0:
                continue
            # 이미 방문한 노드면 스킵
            if MST[next_node]:
                continue
            # 후보군에 추가
            heappush(pq, (graph[node][next_node], next_node))

    return min_weight


T = int(input())  # 테스트 케이스 개수

for tc in range(1, 1 + T):
    V, E = map(int, input().split())  # V: 최대 정점 번호, E: 간선 수

    # 인접행렬 생성 (정점 번호가 0 ~ V 까지 등장하므로 V+1 크기로 만듦)
    graph = [[0] * (V+1) for _ in range(V+1)]

    # 간선 정보 입력
    for _ in range(E):
        start, end, weight = map(int, input().split())
        graph[start][end] = weight
        graph[end][start] = weight  # 무방향 그래프이므로 양쪽 저장

    # Prim 알고리즘 실행 (0번 정점에서 시작)
    result = prim(0)

    # 결과 출력
    print(f'#{tc}', result)
