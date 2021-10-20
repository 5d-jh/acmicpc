import heapq


N = int(input())

heap = []

for _ in range(N):
    num = int(input())
    heapq.heappush(heap, num)

    middle = len(heap) // 2
    if len(heap) % 2 == 0:
        middle -= 1

    print(heapq.nsmallest(middle, heap))
