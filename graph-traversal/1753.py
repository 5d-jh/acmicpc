import math
from queue import PriorityQueue
import sys

input = sys.stdin.readline

def solve(graph, initial):
    distances = [math.inf] * len(graph)
    distances[initial] = 0

    pq = PriorityQueue()
    pq.put((0, initial))

    while not pq.empty():
        distance, current = pq.get()
        
        if distances[current] < distance:
            continue

        if graph[current] is not None:
            for child in graph[current]:
                next_dist, next_node = child
                next_dist += distance
                
                if next_dist < distances[next_node]:
                    distances[next_node] = next_dist
                    pq.put((next_dist, next_node))
    
    return distances


V, E = map(int, input().split(' '))
K = int(input())

graph = [None] * V

for _ in range(E):
    u, v, w = map(int, input().split(' '))
    u -= 1
    v -= 1

    if graph[u] is None:
        graph[u] = []

    graph[u].append((w, v))


for distance in solve(graph, K - 1):
    if distance is math.inf:
        print('INF')
    else:
        print(distance)
