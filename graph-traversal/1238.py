from queue import PriorityQueue
from math import inf
from operator import add, invert
import sys

input = sys.stdin.readline


def solve(rgraph, igraph, students, common_dest):
    sets = (
        (rgraph, [inf] * students),
        (igraph, [inf] * students),
    )

    sets[0][1][common_dest] = 0
    sets[1][1][common_dest] = 0

    for graph, costs in sets:
        pq = PriorityQueue()
        pq.put((0, common_dest))

        while not pq.empty():
            cost, point = pq.get()

            if costs[point] < cost:
                continue

            for child_cost, child_point in graph[point]:
                if cost + child_cost < costs[child_point]:

                    costs[child_point] = cost + child_cost
                    pq.put((cost + child_cost, child_point))
        
    return max(map(add, sets[0][1], sets[1][1]))


N, M, X = map(int, input().split())

graph = [None] * N
igraph = [None] * N
for _ in range(M):
    orig, dest, cost = map(int, input().split())
    orig -= 1
    dest -= 1
    
    if graph[orig] is None:
        graph[orig] = []
    if igraph[dest] is None:
        igraph[dest] = []

    graph[orig].append((cost, dest))
    igraph[dest].append((cost, orig))


print(solve(graph, igraph, N, X - 1))

