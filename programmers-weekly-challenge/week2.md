## 프로그래머스 위클리 챌린지 2주차 - 상호 평가

https://programmers.co.kr/learn/courses/30/lessons/83201
### 소스코드
```py
def solution(scores):
    results = []
    score_avgs = []
    
    for i in range(len(scores)):
        col = []
        for j in range(len(scores)):
            col.append(scores[j][i])
            
        hi_self_evals = list(filter(lambda el: el >= col[i], col))
        lo_self_evals = list(filter(lambda el: el <= col[i], col))
        
        if len(hi_self_evals) == 1 or len(lo_self_evals) == 1:
            del col[i]
        
        score_avgs.append(sum(col) / len(col))
    
    grades = ''
    
    for result in score_avgs:
        if result >= 90:
            grades += 'A'
        elif 80 <= result < 90:
            grades += 'B'
        elif 70 <= result < 80:
            grades += 'C'
        elif 50 <= result < 70:
            grades += 'D'
        else:
            grades += 'F'
            
    return grades
```

#### 해설
단순히 요구 사항에 맞춰 구현하면 된다. 유일한 최대/최솟값은 `filter`를 사용하여 자기 자신 외에 값이 한개인지를 검사했다.

시간 복잡도는 `i`순회 아래 `j` 순회 한 번, `filter` 두 번을 거치므로 `O(n^2)`로 예상한다.
