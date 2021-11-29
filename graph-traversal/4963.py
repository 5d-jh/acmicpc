from typing import Set, Tuple
from collections import deque


def childrenof(not_visited: Set[Tuple[int, int, bool]], point: Tuple[int, int, bool], w, h):
    ops = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    result = []

    x, y = point

    for dx, dy in ops:
        nx, ny = x + dx, y + dy
        inside_range = 0 <= nx < w and 0 <= ny < h
        if inside_range and (nx, ny) in not_visited:
            result.append((nx, ny))

    return result


def solve(not_visited: Set[Tuple[int, int, bool]], w, h):
    result = 0

    while 0 < len(not_visited):
        dq = deque([not_visited.pop()])

        while 0 < len(dq):
            point = dq.pop()
            
            for cx, cy in childrenof(not_visited, point, w, h):
                not_visited.remove((cx, cy))
                dq.appendleft((cx, cy))
        
        result += 1

    return result


w, h = -1, -1
points = set()

while (w, h) != (0, 0):
    w, h = map(int, input().split())

    if (w, h) == (0, 0):
        break

    for i in range(h):
        row = input().split()
        for j in range(w):
            if row[j] == '1':
                points.add((j, i))

    print(solve(points, w, h))
