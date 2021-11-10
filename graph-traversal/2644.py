from collections import deque

def solve(graph, costs, start, end):
    visited = set([start])
    dq = deque([start])

    while 0 < len(dq):
        node = dq.popleft()
        
        for child in graph[node]:
            if child in visited:
                continue

            costs[child] = costs[node] + 1
            visited.add(child)
            dq.append(child)
    
    if costs[end] == 0:
        return -1
    return costs[end]

graph = {}
n = int(input())
start, end = map(int, input().split())
m = int(input())

costs = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    
    graph[a].append(b)
    graph[b].append(a)


print(solve(graph, costs, start - 1, end - 1))
