from queue import PriorityQueue
import sys
import math


input = sys.stdin.readline

def solve(graph, start, end):
    distances = [math.inf] * len(graph)
    distances[start] = 0

    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        weight, selected = pq.get()

        if distances[selected] < weight:
            continue

        if graph[selected] is not None:
            for wchild, schild in graph[selected]:
                if wchild + weight < distances[schild]:
                    distances[schild] = wchild + weight
                    pq.put((wchild + weight, schild))
    
    return distances[end]



N = int(input())
M = int(input())

graph = [None] * N

for _ in range(M):
    s, d, w = map(int, input().split())
    s -= 1
    d -= 1

    if graph[s] is None:
        graph[s] = []

    graph[s].append((w, d))
    

A, B = map(int, input().split())

print(solve(graph, A - 1, B - 1))
