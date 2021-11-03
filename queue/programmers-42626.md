## 프로그래머스 42626
https://programmers.co.kr/learn/courses/30/lessons/42626#
### 소스코드
```py
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    result = 0
    last = 0
    
    while 1 < len(scoville):
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        if K <= a:
            break
        
        last = a + (b * 2)
        
        heapq.heappush(scoville, last)
        result += 1
    
    if len(scoville) == 1 and heapq.heappop(scoville) < K:
        return -1
    
    return result
```

### 해설
`scoville`의 길이가 1이 되거나, `a`가 `K`보다 작은 동안,
1. 가장 낮은 스코빌과 두 번째로 낮은 스코빌을 꺼낸다.
1. 주어진 식에 따라 스코빌을 계산한다.
1. `scoville`에 삽입한다.
1. `result`를 1 증가시킨다.

만약 반복이 끝나고 `scoville`의 길이가 1이라면, `a`가 K 보다 큰 적이 없던 경우이다. 가장 마지막 조합이 `scoville`에 들어 있을 것이므로 `K`보다 큰지 검사한다. 여전히 작으면 -1을 리턴한다. 그렇지 않으면 `result`를 리턴한다.
