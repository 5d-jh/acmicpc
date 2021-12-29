## 프로그래머스 있었는데요 없었습니다 
https://programmers.co.kr/learn/courses/30/lessons/59043

> 관리자의 실수로 일부 동물의 입양일이 잘못 입력되었습니다. 보호 시작일보다 입양일이 더 빠른 동물의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일이 빠른 순으로 조회해야합니다.

### 소스코드
```sql
SELECT INS.ANIMAL_ID, INS.NAME FROM ANIMAL_INS INS
INNER JOIN ANIMAL_OUTS OUTS ON
    INS.ANIMAL_ID = OUTS.ANIMAL_ID
    AND OUTS.DATETIME < INS.DATETIME
ORDER BY INS.DATETIME ASC
```

### 해설
`ANIMAL_ID` 기준으로 입양일이 보호 시작일보다 이르면서 각 테이블의 id가 같은 것을 기준으로 inner join한 후, `INS.DATETIME` 기준으로 오름차순 정렬한다.