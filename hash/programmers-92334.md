## 프로그래머스 92334
https://programmers.co.kr/learn/courses/30/lessons/92334

### 소스코드
```py
def solution(id_list, report, k):
    report_count = {}
    reported_by = {}
    
    for r in report:
        reporter, reported = r.split()
        
        if reported not in report_count:
            report_count[reported] = 0
        
        if reporter not in reported_by:
            reported_by[reporter] = set()

        # [1]
        if reported not in reported_by[reporter]:
            report_count[reported] += 1
        
        # [2]
        reported_by[reporter].add(reported)
    
    result = []
    
    for id in id_list:
        if id not in reported_by:
            result.append(0)
            continue
        
        turned_in = 0
        # [3]
        for reported in reported_by[id]:
            if report_count[reported] >= k:
                turned_in += 1
        result.append(turned_in)
    
    return result

print(solution(['con', 'ryan'], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

```

### 해설
* `report_count`: 신고당한 사람 id 기준 신고당한 횟수
* `reported_by`: 신고한 사람 id 기준 신고한 사람들

A가 B를 신고할 때, B가 A에 신고된 적이 없다면 `report_count[B]`를 1 증가시킨다[1]. 또한 `reported_by[A]`에 B를 삽입한다[2].

해당 규칙대로 삽입이 완료되면, `id_list` 기준으로 순회하며 A가 신고한 사람들을 찾는다[3].

만약 A가 신고한 사람이 B라면, `report_count[B]`를  참조하여 B가 신고당한 횟수를 찾는다. 그 횟수가 `k` 이상이면 `turned_in`을 1 증가시킨다.

`result`에 `turned_in`을 삽입한 후 리턴한다.
