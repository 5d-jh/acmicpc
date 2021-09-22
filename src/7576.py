from collections import deque


def childrenof(points: set, point, width, height):
    operations = (
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    )

    results = []

    x, y = point

    for dx, dy in operations:
        nx, ny = dx + x, dy + y
        
        inside_range = 0 <= nx < width and 0 <= ny < height
        if inside_range and (nx, ny) in points:
            results.append((nx, ny))
    
    return results



def solve(points: set, starting_points: set, width: int, height: int):
    dq = deque(starting_points)

    distances = []
    for _ in range(height):
        distances.append([0] * width)

    while 0 < len(dq):
        point = dq.pop()

        children = childrenof(points, point, width, height)
        for child in children:
            points.remove(child)
            dq.appendleft(child)

            x, y = point
            cx, cy = child
            distances[cy][cx] = distances[y][x] + 1

    if 0 < len(points):
        return -1

    return max(map(max, distances))


M, N = map(int, input().split())

points = set()
starting_points = set()

for i in range(N):
    row = input().split()

    for j in range(M):
        if row[j] == '0':
            points.add((j, i))
        elif row[j] == '1':
            starting_points.add((j, i))


print(solve(points, starting_points, M, N))
