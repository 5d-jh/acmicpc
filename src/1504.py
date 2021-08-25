from math import inf, isinf
from queue import PriorityQueue
from typing import List
import sys

input = sys.stdin.readline


def djikstra(graph, pivot) -> List[int]:
    costs = [inf] * len(graph)
    pq = PriorityQueue()
    pq.put((0, pivot))

    while not pq.empty():
        cost, point = pq.get()
        
        if costs[point] < cost:
            continue
        
        if graph[point] is not None:
            for child_cost, child_point in graph[point]:
                if cost + child_cost < costs[child_point]:
                    costs[child_point] = cost + child_cost
                    pq.put((cost + child_cost, child_point))
    
    return costs


def solve(graph, v1, v2):
    costs = djikstra(graph, v1)
    v1_v2 = costs[v2]

    if v1 == 0 or v2 == 0:
        return -1 if isinf(v1_v2) else v1_v2
    
    costs = djikstra(graph, 0)
    a_v1 = costs[v1]
    a_v2 = costs[v2]

    costs = djikstra(graph, len(graph) - 1)
    v1_dest = costs[v1]
    v2_dest = costs[v2]

    a_v1_v2_dest = a_v1 + v1_v2 + v2_dest
    a_v2_v1_dest = a_v2 + v1_v2 + v1_dest

    result = min(a_v1_v2_dest, a_v2_v1_dest)

    if isinf(result):
        return -1

    return result


N, E = map(int, input().split())

graph = [None] * N
for _ in range(E):
    a, b, cost = map(int, input().split())
    a -= 1
    b -= 1

    if graph[a] is None:
        graph[a] = []
    if graph[b] is None:
        graph[b] = []

    graph[a].append((cost, b))
    graph[b].append((cost, a))

v1, v2 = map(int, input().split())
print(solve(graph, v1 - 1, v2 - 1))
