import heapq
from typing import List


def solve(A: List, B: List):
    result = 0

    while 0 < len(A):
        _, a = heapq.heappop(A)
        _, b = heapq.heappop(B)
        result += a * b
    
    return result


N = int(input())
A = []
B = []

elems = map(int, input().split())
for el in elems:
    heapq.heappush(A, (el, el))

elems = map(int, input().split())
for el in elems:
    heapq.heappush(B, (-el, el))

print(solve(A, B))
