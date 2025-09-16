# # 그래프 , 인접 행렬 방식
# V, E = map(int, input().split())
# data = list(map(int, input().split()))
#
# adj_matrix = [[0] * (V+1) for _ in range(V+1)]
#
# for i in range(E):
#     n1, n2 = data[i*2] , data[i*2+1]
#     adj_matrix[n1][n2] = 1
#     adj_matrix[n2][n1] = 1
#
# for row in adj_matrix:
#     print(row)

# # 그래프, 인접 리스트 방식
# V, E = map(int, input().split())
# data = list(map(int, input().split()))
#
# adj_list = [[]for _ in range(V+1)]
#
# for i in range(E):
#     n1, n2 = data[i*2] , data[i*2+1] # n1이 받는게 부모, n2가 자식
#     adj_list[n1].append(n2)
#     adj_list[n2].append(n1)
#
# for i in range(1, V + 1):
#     print(f'{i} : {adj_list[i]}')

# import sys
# sys.stdin = open('input.txt')
#
# def matrix(current_node, adj_list, visited, path):
#     visited[current_node] = True
#     path.append(current_node)
#
#     for next_node in adj_list[current_node]:
#         if not visited[next_node]:
#             matrix(next_node, adj_list, visited, path)
#
#
# V , E = map(int, input().split())
# data = list(map(int, input().split()))
#
# adj_list = [[] for _ in range(V+1)]
#
# for i in range(E):
#     n1, n2 = data[i*2], data[i*2+1]
#     adj_list[n1].append(n2)
#     adj_list[n2].append(n1)
#
# # print(adj_list)
# visited = [False] * (V + 1)
# traversal_path = []
# matrix(1, adj_list, visited, traversal_path)
# print(''.join(map(str, traversal_path)))

# import sys
# sys.stdin = open('input.txt')
# from collections import deque
#
# def bfs_list(start_node , V ,adj_list):
#     visited = [False] * (V+1)
#     path = []
#     q = deque()
#     visited[start_node] = True
#     q.append(start_node)
#
#     while q:
#         current_node = q.popleft()
#         path.append(current_node)
#         for next_node in sorted(adj_list[current_node]):
#             if not visited[next_node]:
#                 visited[next_node] = True
#                 q.append(next_node)
#     return path
#
#
#
# V, E = map(int, input().split())
# data = list(map(int, input().split()))
# adj_list = [[] for _ in range(V+1)]
# for i in range(E):
#     n1, n2 = data[i*2] , data[i*2+1]
#     adj_list[n1].append(n2)
#     adj_list[n2].append(n1)
#
# print(adj_list)
# print(sorted(adj_list))
# result_path = bfs_list(1, V, adj_list)
# print(''.join(map(str,result_path)))

import heapq
# heap = []
# heapq.heappush(heap, 5)
# heapq.heappush(heap, 1)
# heapq.heappush(heap, 7)
# print(heap)
# small = heapq.heappop(heap)
# print(small)
# print(heap)

arr = [5,3,8,4,1,2]
print(arr)
heapq.heapify(arr)
print(arr)
heapq.heappop(arr)
print(arr)





























































