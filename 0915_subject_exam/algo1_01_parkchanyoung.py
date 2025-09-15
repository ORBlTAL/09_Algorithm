"""
단순 증가 패턴을 구하는 문제
윈도우로 나눈 범위에서 모두에 대해 단순 증가인지 구하는 경우보다는 역으로 단순 증가가 안되는 경우를 세는것이
구현하기에 더 간단할 것으로 판단됨
역이 발견되면 그떄의 경우를 세주고 나머지는 무시, 그 다음 슬라이드로 넘어가게 구현
모두 단순 증가일 경우 그 개수는 M인데, M에서 역을 발견한 수를 빼서 최종 출력
"""
import sys
sys.stdin = open('input.txt')

def calc(arr):
    global cnt # cnt 계산을 위해 글로벌로 선언
    for i in range(M): # 리스트를 윈도우 수만큼 나눠주기 위한 범위
        for j in range(M-1): # 나눈 윈도우 내에서 앞뒤 값끼리 비교하기 위한 범위
            if 0<= i*M+j < N and 0<=i*M+j+1 < N: # 인덱스 에러 방지를 위해 리스트 최대 길이인 N을 넘어가지 않게 함
                if arr[i*M+j] >= arr[i*M+j+1]: # 앞에 값이 뒤보다 크거나 같으면 단순증가가 아님
                    cnt +=1 # 그때의 경우를 세줌
                    break # break사용, 한번이라도 발생하면 단순증가가 성립하지 않으므로, 발생한 이후는 무시
                          # break를 사용함으로써 이중 for문중 안쪽 for문은 정지되고, 바깥쪽 for문은 다음으로 넘어감

T = int(input())
for tc in range(1, 1 + T):
    N , M = map(int,input().split())
    arr = list(map(int, input().split()))
    cnt = 0 # 단순증가패턴에 성립하지 않을 경우를 세는 cnt

    max_val = N // M # max_val는 발생할 수 있는 최대 단순증가패턴의 개수임
    if N % M > 0: # 전체 정수의 개수에서 윈도우의 크기를 나눈 값에, 만약 나머지가 0보다 큰 경우 + 1을 해서 구함
        max_val +=1
    calc(arr) # 단순증가패턴이 없는 경우의 개수를 세기위한 함수 calc
    print(f'#{tc}', max_val - cnt) # 단순증가패턴을 가지는 윈도우의 수 출력

