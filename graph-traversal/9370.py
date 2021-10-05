from queue import PriorityQueue
import sys


input = sys.stdin.readline

def do_djikstra(graph, num_points, starting_point):
    costs = [int(1e9)] * num_points

    pq = PriorityQueue()
    pq.put((0, starting_point))

    while not pq.empty():
        weight, point = pq.get()

        if costs[point] < weight:
            continue

        if graph[point] is not None:
            for wchild, pchild in graph[point]:
                if weight + wchild < costs[pchild]:
                    costs[pchild] = weight + wchild
                    pq.put((weight + wchild, pchild))
    
    return costs


def solve(graph, num_points, start, end_candidates, sniffs):
    g, h = sniffs
    start_to = do_djikstra(graph, num_points, start)
    g_to = do_djikstra(graph, num_points, g)
    h_to = do_djikstra(graph, num_points, h)

    result = []

    for candidate in end_candidates:
        gh = start_to[g] + g_to[h] + h_to[candidate] == start_to[candidate]
        hg = start_to[h] + h_to[g] + g_to[candidate] == start_to[candidate]
        if gh or hg:
            result.append(candidate + 1)
    
    return sorted(result)


T = int(input())

result = []

for _ in range(T):
    candidates = []
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    s -= 1
    g -= 1
    h -= 1

    graph = {}

    for _ in range(m):
        a, b, d = map(int, input().split())
        a -= 1
        b -= 1

        if a not in graph:
            graph[a] = [(0, a)]
        if b not in graph:
            graph[b] = [(0, b)]

        graph[a].append((d, b))
        graph[b].append((d, a))

    for _ in range(t):
        candidates.append(int(input()) - 1)

    result.append(solve(graph, n, s, candidates, (g, h)))


for r in result:
    print(*r)
