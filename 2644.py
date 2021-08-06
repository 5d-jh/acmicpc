from collections import deque


n_people = int(input())
start, end = input().split(' ')
start, end = int(start), int(end)
n_edges = int(input())

graph = {}

for _ in range(n_edges):
    v1, v2 = input().split(' ')
    v1, v2 = int(v1), int(v2)
    
    if v1 not in graph:
        graph[v1] = []

    if v2 not in graph:
        graph[v2] = []

    graph[v1].append(v2)
    graph[v2].append(v1)



def do_bfs(v):
    dq = deque([v])
    visited = set()
    count = 0
    
    while len(dq) > 0:
        n = dq.pop()

        visited.add(n)

        count += 1

        valid_children = 0
        for child in graph[n]:
            if child == end:
                return len(visited)

            if child not in visited:
                valid_children += 1
                dq.appendleft(child)
                
        if valid_children == 0 or len(graph[n]) == 1:
            count -= 1
    

print(graph)
print(do_bfs(start))
