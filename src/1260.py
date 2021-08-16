from collections import deque


N, M, V = map(int, input().split())

graph = {}

for _ in range(M):
    a, b = input().split()
    a = int(a)
    b = int(b)

    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)


# print(graph)


dfs_visited = set()

def dfs(v):
    print(v, end=' ')
    dfs_visited.add(v)
    
    children = graph[v]
    for child in sorted(children):
        if child not in dfs_visited:
            dfs(child)

try:
    dfs(V)
    print()
except:
    pass


bfs_visited = set()

def bfs(v):
    d = deque([v])
    
    while(len(d) > 0):
        root = d.pop()

        if root not in bfs_visited:
            print(root, end=' ')
        bfs_visited.add(root)

        for child in sorted(graph[root]):
            if child not in bfs_visited:
                d.appendleft(child)

try:
    bfs(V)
    print()
except:
    pass
