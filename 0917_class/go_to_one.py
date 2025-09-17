"""
1251. 하나로
다 연결 + 최소 비용 => MST로 구현하는 문제
"""

import sys
sys.stdin = open('input.txt')

# 1. 각 섬을 연결하는 간선들을 만들자
# 2. MST 구성 (prim, kruskal)
# 섬이 1000개라면 간선의 수 : 1000*999 => 1000*1000 => 백만개..?

def find_set(x):
    if x == parents[x]: # 대표자 발견했다면 종료
        return x

    # 경로 압축 코드
    parents[x] = find_set(parents[x])
    return find_set(parents[x])

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)

    if rx == ry: # 이미 같은 집합이면 병합 x
        return
    parents[ry] = rx # 병합

T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    tax = float(input())

    edges = []
    for i in range(N):
        for j in range(i+1, N):
            # x좌표차이 ** 2 + y 좌표차이 ** 2 * 세율
            cost = ((x_list[i] - x_list[j]) ** 2 + (y_list[i] - y_list[j]) ** 2) * tax
            edges.append((i, j, cost))

    # 2. 가중치 기준 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    # 3. 싸이클 검사하면서, 앞에서부터 간선들을 선택
    # --> 언제까지? MST 완성 (N-1 개 선택까지)
    parents = [i for i in range(N)] # make-set

    cnt = 0
    min_cost = 0
    for u, v, w in edges:
        if find_set(u) != find_set(v): # 같은 집합이 아니라면
            union(u, v)

            min_cost += w
            cnt += 1

        if cnt == N - 1:
            break
    print(f'#{tc} {min_cost:.0f}')








import sys
sys.stdin = open('input.txt')

# 서로소 집합(Disjoint Set) 자료구조 - find 연산
def find_set(x):
    if x == parents[x]:  # x가 대표자라면 그대로 반환
        return x

    # 경로 압축 적용
    parents[x] = find_set(parents[x])
    return find_set(parents[x])

# 서로소 집합 - union 연산
def union(x, y):
    rx = find_set(x)  # x의 대표자
    ry = find_set(y)  # y의 대표자

    if rx == ry:  # 이미 같은 집합이라면 합치지 않음
        return
    parents[ry] = rx  # y 집합을 x 집합에 병합

# 테스트 케이스 수 입력
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())  # 섬의 개수
    x_list = list(map(int, input().split()))  # 각 섬의 x 좌표
    y_list = list(map(int, input().split()))  # 각 섬의 y 좌표
    tax = float(input())  # 환경 부담 세율(세금)

    edges = []  # 모든 간선 후보를 저장할 리스트
    for i in range(N):
        for j in range(i+1, N):
            # 두 섬 사이의 거리 제곱 * 세율 = 비용
            cost = ((x_list[i] - x_list[j]) ** 2 + (y_list[i] - y_list[j]) ** 2) * tax
            edges.append((i, j, cost))

    # 2. 간선들을 비용 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    # 3. MST 구하기 (크루스칼 알고리즘)
    parents = [i for i in range(N)]  # make-set: 각 노드를 자기 자신으로 초기화

    cnt = 0  # 선택한 간선 수
    min_cost = 0  # 최소 비용 누적합
    for u, v, w in edges:
        if find_set(u) != find_set(v):  # 같은 집합이 아니라면 (사이클이 생기지 않음)
            union(u, v)  # 두 집합을 합침
            min_cost += w  # 비용 추가
            cnt += 1

        if cnt == N - 1:  # MST는 N-1개의 간선이 선택되면 완료
            break

    # 결과 출력 (소수점 첫째자리에서 반올림 후 정수형으로)
    print(f'#{tc} {min_cost:.0f}')





















