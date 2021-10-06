import math
from queue import PriorityQueue


def childrenof(x, y, lim_x, lim_y):
    children = []
    
    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for vx, vy in directions:
        if lim_x > x + vx >= 0 and lim_y > y + vy >= 0:
            children.append((x + vx, y + vy))

    print

    return children


def solve(matrix, xsize, ysize):
    costs = []
    for _ in range(ysize):
        costs.append([math.inf] * xsize)

    pq = PriorityQueue()
    pq.put((0, (0, 0)))

    while not pq.empty():
        cost, pos = pq.get()
        x, y = pos

        if costs[y][x] < cost:
            continue

        for child_x, child_y in childrenof(x, y, xsize, ysize):
            wall = min(1, matrix[child_y] & (2 ** child_x)) # 1 or 0

            if cost + wall < costs[child_y][child_x]:
                pq.put((cost + wall, (child_x, child_y)))
                costs[child_y][child_x] = cost + wall
    
    result = costs[ysize - 1][xsize - 1]

    if result is math.inf:
        return 0
    else:
        return result


M, N = map(int, input().split())

matrix = []

for n in range(N):
    row_string = input()
    bitmask = 0

    for m in range(M):
        if row_string[m] == '1':
            bitmask += 2 ** m
    
    matrix.append(bitmask)

print(solve(matrix, M, N))
