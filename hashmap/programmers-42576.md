## 프로그래머스 42576
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3

### 소스코드
```py
def solution(participant, completion):
    counts = {}
    
    for p in participant:
        if p not in counts:
            counts[p] = 0
        counts[p] += 1
    
    for c in completion:
        counts[c] -= 1
        if counts[c] <= 0:
            del counts[c]
        
    
    return list(counts.keys())[0]
```

### 해설
고딩 때 머리 싸매면서 못풀었던 문제. counts라는 맵에서 카운팅을 한 후 `completion` 기반으로 카운트를 빼주면 된다.
