# 1. 각 집합을 만들어주는 함수
def make_set(n):
    # 1~n 까지의 원소가 "각자 자기 자신이 대표자라고 설정"
    parents = [i for i in range(n + 1)] # 자기 자신을 그대로 넣어줘서 return
    ranks = [0] * (n + 1) # rank를 모두 0으로 초기화
    return parents

# 2. 집합의 대표자를 찾는 함수
def find_set(x):
    # 자신 == 부모 -> 해당 집합의 대표자
    if x == parents[x]:
        return x
    return parents[x]

# 경로 압축 추가 코드
def find_set(x):
    # 자신 == 부모 -> 해당 집합의 대표자
    if x == parents[x]:
        return x
    # 경로 압축 (path compression) 코드
    # - 내가 대표자를 바로 가리키도록
    parents[x] = find_set(parents[x])
    return parents[x]

# 3. 두 집합을 합치는 함수
def union(x, y):
    # 1. x, y의 대표자를 검색
    rep_x = find_set(x)
    rep_y = find_set(y)
    # 만약 이미 같은 집합
    if rep_x == rep_y:
        return # 같은 집합끼리는 합칠 필요가 없다

    # 더 작은쪽으로 연결하는 문제라면, 조건을 추가해준다.
    if rep_x < rep_y:
        parents[rep_y] = rep_x
    else:
        parents[rep_x] = rep_y

    # 덩치가 더 작은 집합(==rank 가 더 낮은 집합)이 더 큰 집합 밑으로 가야한다.
    if ranks[rep_x] < ranks[rep_y]:
        parents[rep_x] = rep_y
    elif ranks[rep_x] > ranks[rep_y]:
        parents[rep_y] = rep_x
    else:
        # rank가 동일하다
        # -> 한 쪽으로 병합하고, 대표자의 rank를 + 1
        parents[rep_y] = rep_x
        ranks[rep_x] += 1

N = 6
parents, ranks = make_set(N)

union(2, 4)
union(4, 6)

if find_set(2) == find_set(6):
    print("2와 6은 같은 집합")
else:
    print("다른 집합")
