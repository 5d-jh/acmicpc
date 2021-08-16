n_computer = int(input())
n_edges = int(input())

graph = {}

for _ in range(n_edges):
    a, b = input().split(' ')
    a, b = int(a), int(b)

    if a not in graph:
        graph[a] = []

    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)


visited = set()
result = -1 #do not count 1
def do_dfs(v):
    global result
    result += 1
    visited.add(v)

    for child in graph[v]:
        if child not in visited:
            do_dfs(child)

do_dfs(1)
print(result)
