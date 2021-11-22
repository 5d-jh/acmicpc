## 프로그래머스 59405
https://programmers.co.kr/learn/courses/30/lessons/59405

> 동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요. 

### 소스코드
```sql
SELECT NAME FROM ANIMAL_INS ORDER BY DATETIME ASC LIMIT 1
```

### 해설
`ORDER BY DATETIME ASC`로 `DATETIME`기준으로 정렬한 다음 `LIMIT 1`으로 한 행만 나오도록 출력한다.
