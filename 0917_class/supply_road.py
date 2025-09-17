"""
(누적거리 , y, x 좌표)
전형적인 다익스트라 문제
그래프 문제와 차이점
 - 이동 가능한 게 상하좌우 4개 방향
 - 최단 거리를 저장할 리스트를 2차원으로 구성해야 한다
    - [기존] 특정 노드까지 가는 최단거리
    - [문제] 특정 좌표까지 가는 최단거리
 - heapq에 들어가야 할 데이터 (누적거리 , y, x) 형태
"""
import sys
from heapq import heappop, heappush

sys.stdin = open('input2.txt')


def dijkstra():
    dists = [[21e8] * N for _ in range(N)]  # 최단거리를 저장할 2차원 리스트
    dists[0][0] = 0  # 시작점 초기화
    pq = [(0, 0, 0)]  # (누적거리, y, x)
    while pq:
        dist, y, x = heappop(pq)
        for i in range(4):  # 상하좌우 확인
            ny = y + dy[i]
            nx = x + dx[i]
            # 범위 밖이면 다음 방향 확인
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            # 누적거리 계산 = 현재까지의 거리 + 다음 거리
            new_dist = dist + graph[ny][nx]

            # 이미 더 작거나 같은 시간으로 온 적이 있다
            if dists[ny][nx] <= new_dist:
                continue

            dists[ny][nx] = new_dist
            heappush(pq, (new_dist, ny, nx))

    return dists[N - 1][N - 1]


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]

    result = dijkstra()
    print(f'#{tc} {result}')







import sys
from heapq import heappop, heappush

sys.stdin = open('input2.txt')

def dijkstra():
    # 모든 좌표까지의 최단 거리를 저장할 2차원 리스트 (처음엔 무한대 값으로 채움)
    dists = [[21e8] * N for _ in range(N)]
    dists[0][0] = 0  # 시작점 (0,0)의 최단거리를 0으로 초기화

    # 우선순위 큐: (현재까지의 누적거리, 현재 y 좌표, 현재 x 좌표)
    pq = [(0, 0, 0)]

    while pq:
        dist, y, x = heappop(pq)  # 현재까지의 누적거리가 가장 작은 위치 꺼냄

        # 현재 위치에서 4방향(상, 하, 좌, 우) 탐색
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # 범위를 벗어나면 무시
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            # 새로운 누적거리 = 현재까지 거리 + 다음 칸의 비용
            new_dist = dist + graph[ny][nx]

            # 기존에 저장된 거리보다 더 짧은 경로가 발견되었을 경우에만 갱신
            if dists[ny][nx] <= new_dist:
                continue

            dists[ny][nx] = new_dist
            heappush(pq, (new_dist, ny, nx))  # 큐에 새로운 상태 추가

    # 도착점 (N-1, N-1)의 최단 거리 반환
    return dists[N - 1][N - 1]


# 방향 벡터 (상, 하, 좌, 우)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 테스트 케이스 입력
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())  # 격자의 크기
    # 지도 입력 (문자열로 들어온 값을 정수 리스트로 변환)
    graph = [list(map(int, input())) for _ in range(N)]

    # 다익스트라 실행
    result = dijkstra()

    # 결과 출력
    print(f'#{tc} {result}')
