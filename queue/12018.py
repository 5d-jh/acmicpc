from typing import Dict, List
import heapq
import sys


input = sys.stdin.readline

def solve(subjects_info: List[Dict], mileage: int):
    invests = []
    
    for info in subjects_info:
        if len(info['mileages']) < info['capacity']:
            heapq.heappush(invests, 1)
            continue

        hq = []
        for m in info['mileages']:
            heapq.heappush(hq, -m)

        for _ in range(info['capacity'] - 1):
            heapq.heappop(hq)
        
        heapq.heappush(invests, -heapq.heappop(hq))

    result = 0
    while mileage > 0 and len(invests) > 0:
        mileage -= heapq.heappop(invests)
        result += 1

    if mileage < 0:
        result -= 1
    
    return result
    

_subject_info = []

_n, _m = map(int, input().split())
for _ in range(_n):
    applicant, capacity = map(int, input().split())
    mileages = list(map(int, input().split()))
    _subject_info.append({
        'applicant': applicant,
        'capacity': capacity,
        'mileages': mileages
    })

print(solve(_subject_info, _m))
