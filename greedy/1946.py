from typing import List
import heapq
import sys


input = sys.stdin.readline


def solve(ord_paper: List):
    _, top_interview = heapq.heappop(ord_paper)

    result = 1

    while 0 < len(ord_paper):
        _, interview = heapq.heappop(ord_paper)
        
        if interview < top_interview:
            result += 1
            top_interview = interview
    
    
    return result


T = int(input())
for _ in range(T):
    N = int(input())

    ord_paper = []

    for i in range(N):
        paper, interview = map(int, input().split())
        heapq.heappush(ord_paper, (paper, interview))
    
    print(solve(ord_paper))

