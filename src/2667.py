from collections import deque

def childrenof(len_matrix: int, points: set, point):
    operations = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    )

    x, y = point

    result = []

    for dx, dy in operations:
        nx, ny = x + dx, y + dy

        inside_graph = 0 <= nx < len_matrix and 0 <= ny < len_matrix

        if inside_graph and (nx, ny) in points:
            result.append((nx, ny))

    return result


def solve(N: int, points: set):
    result = []

    while 0 < len(points):
        dq = deque()
        dq.appendleft(points.pop())

        homes = 1
    
        while 0 < len(dq):
            current = dq.pop()

            for cx, cy in childrenof(N, points, current):
                points.remove((cx, cy))
                dq.appendleft((cx, cy))
                homes += 1
        
        result.append(homes)

    return len(result), sorted(result)


N = int(input())

available_points = set()

for i in range(N):
    row = list(input())

    for j, elem in enumerate(row):
        if elem == '1':
            available_points.add((j, i))


len_result, result = solve(N, available_points)
print(len_result)

for r in result:
    print(r)
