import sys
sys.stdin = open('input2.txt')
T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    # 시작시간, 끝나는 시간 둘 다 오름차순으로 정렬 -> 현재 끝나는 시간이 다음 시작시간보다 작거나 같을 때
    # 현재시간을 다음 시간으로 스왑하고, 카운트 해주면 될 듯?
    arr.sort(key=lambda x:x[1])
    now = arr[0]
    cnt = 1
    for i in range(N-1):
        if now[1] <= arr[i+1][0]:
            now = arr[i+1]
            cnt +=1
    print(f'#{tc}',cnt)