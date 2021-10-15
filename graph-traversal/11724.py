from collections import deque
from typing import Dict, Set
import sys


input = sys.stdin.readline


def do_dfs(graph: Dict, not_visited: Set):
    dq = deque()
    dq.append(not_visited.pop())

    while 0 < len(dq):
        point = dq.popleft()
        
        for child in filter(lambda el: el in not_visited, graph[point]):
            not_visited.remove(child)
            dq.appendleft(child)


def solve(graph: Dict, result: int):
    not_visited = set(graph.keys())

    while 0 < len(not_visited):
        do_dfs(graph, not_visited)
        result += 1
    
    return result



N, M = map(int, input().split())

graph = {}

for _ in range(M):
    u, v = map(int, input().split())
    
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []

    graph[u].append(v)
    graph[v].append(u)


print(solve(graph, N - len(graph.keys())))
