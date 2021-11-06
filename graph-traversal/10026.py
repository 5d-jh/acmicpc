from typing import List, Set
from collections import deque


def childrenof(N: int, graph: Set, point) -> List:
    ops = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    )

    result = []

    x, y, color = point

    for dx, dy in ops:
        nx, ny = x + dx, y + dy

        inside_range = 0 <= nx < N and 0 <= ny < N
        if inside_range and (nx, ny, color) in graph:
            result.append((nx, ny, color))
    
    return result


def dfs(N: int, graph: Set):
    result = 0

    while 0 < len(graph):
        dq = deque()
        dq.appendleft(graph.pop())

        while 0 < len(dq):
            x, y, color = dq.pop()

            children = childrenof(N, graph, (x, y, color))
            for child in children:
                dq.appendleft(child)
                graph.remove(child)

        result += 1
    
    return result


N = int(input())
graph = set()
graph_rgweak = set()
for i in range(N):
    row = list(input())
    for j, color in enumerate(row):
        if color == 'G':
            graph_rgweak.add((j, i, 'R'))
        else:
            graph_rgweak.add((j, i, color))

        graph.add((j, i, color))


print(dfs(N, graph), dfs(N, graph_rgweak))
