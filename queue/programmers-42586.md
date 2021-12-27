## 프로그래머스 42586
https://programmers.co.kr/learn/courses/30/lessons/42586#
### 소스코드
```py
from collections import deque


def solution(progresses, speeds):
    estimate = deque()
    
    for p, s in zip(progresses, speeds):
        rest = 0 if (100 - p) % s == 0 else 1
        estimate.append((100 - p) // s + rest)
    
    maxval = estimate.popleft()
    results = []
    result = 1
    
    while 0 < len(estimate):
        est = estimate.popleft()
        
        if maxval < est:
            results.append(result)
            maxval = est
            result = 1
        else:
            result += 1
            
    results.append(result)
            
    return results
```

### 해설
progress, speeds에 따른 소요 기간을 산정한 `estimate` 배열을 만든다.

`estimate` 배열을 순차적으로 탐색하며 최대값이 갱신되는 순간 결과 배열에 `result`를 삽입한다.
