"""
첫번째 시작점이 다음 시작점보다 작고 끝점이 다음 끝점보다 클 때 또는 시작점이 다음 시작점보다 크고 끝점이 다음 끝점보다 작을 때
이떄마다 간선이 생기므로 그 떄마다 카운트 해줌
순서는 첫번째 점과 바로 다음점들 끼리 하나씩 조회하고 모두 끝마치면 두번째 점이 그 다음점들과 조회하게끔 구현함.
"""
import sys
sys.stdin = open('input2.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    i = 0 # while문 횟수 제한 , N-1번만큼 조회하게 함
    state = 0 # 첫번쨈 점이 그 다음점부터 끝까지, 두번째 점이 그 다음점부터 끝까지 조회할 수 있도록 인덱스를 지정
    cnt = 0 # 카운트 변수 cnt를 0으로 초기화
    while i < N-1:
        for j in range(state, N-1): # 첫 while문에서는 0 부터 N-1, 그 다음은 1 부터 N-1, 이런식으로 범위를 좁혀감
            # arr의 첫번째와 두번째 좌표로 설명하자면 [0][0] 과 [1][0] / [0][1] 과 [0][0]을 조사해 교차점이 생기는지 확인. 즉 시작점과 끝점을 조사
            if (arr[state][0] < arr[1+j][0] and arr[state][1] > arr[1+j][1]) or (arr[state][0] > arr[1+j][0] and arr[state][1] < arr[1+j][1]):
                cnt +=1
        i+=1
        state+=1 # for문 끝나면 첫번째 점이 아니라 두번째 점부터 시작해야 하므로 +1

    print(f'#{tc}',cnt)
