# arr = list(range(1,11))
# def calc(result):
#     if result == 10:
#         return
#

arr = list(range(1,11))
path = []

def calc(cnt, idx):
    if sum(path) == 10:
        print(*path)
        return
    if sum(path) > 10:
        return
    if idx == len(arr):
        return
    for i in range(idx, len(arr)):
        path.append(arr[i])
        calc(cnt+1, i+1)
        path.pop()

calc(0, 0)




