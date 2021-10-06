## 프로그래머스 59044
https://programmers.co.kr/learn/courses/30/lessons/59044

> 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.

### 소스코드
```sql
SELECT AI.NAME, AI.DATETIME FROM ANIMAL_INS AI LEFT JOIN ANIMAL_OUTS AO ON AI.ANIMAL_ID = AO.ANIMAL_ID WHERE AO.ANIMAL_ID IS NULL ORDER BY AI.DATETIME ASC LIMIT 3
```

### 해설
`ANIMAL_ID` 기준으로 조인후 `ANIMAL_OUTS` 쪽의 id가 null값인 부분만 선택한다.