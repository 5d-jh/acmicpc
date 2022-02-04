## 프로그래머스 42576
https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3#fn1

### 소스코드
```py
def solution(lottos, win_nums):
    non_zeros = list(filter(lambda l: l != 0, lottos))
    
    win_num_counts = {}
    for n in win_nums:
        if n not in win_num_counts:
            win_num_counts[n] = 0
        
        win_num_counts[n] += 1
    
    fails = 0
    for l in non_zeros:
        if l in win_num_counts:
            win_num_counts[l] -= 1
            
            if win_num_counts[l] == 0:
                del win_num_counts[l]
        else:
            fails += 1
    
    zeros = len(list(filter(lambda l: l == 0, lottos)))
    return [min(6, fails + 1), min(6, zeros + fails + 1)]
```

### 해설
* `non_zeros`: 낙서되지 않은 로또번호들
* `fails`: 실패가 확정된 로또번호의 개수
`win_num_counts`로 로또번호에 대한 빈도를 기록한 다음 `non_zeros`를 순회&차감하며 0이 되면 키를 삭제한다.

키가 존재하지 않으면 `fails`를 증가시킨다. 그 후 0이 다 맞는 경우와 0이 다 틀린 경우 등수를 리턴한다.
