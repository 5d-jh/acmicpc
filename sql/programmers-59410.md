## 프로그래머스 77487
https://programmers.co.kr/learn/courses/30/lessons/59410

> 입양 게시판에 동물 정보를 게시하려 합니다. 동물의 생물 종, 이름, 성별 및 중성화 여부를 아이디 순으로 조회하는 SQL문을 작성해주세요. 이때 프로그래밍을 모르는 사람들은 NULL이라는 기호를 모르기 때문에, 이름이 없는 동물의 이름은 "No name"으로 표시해 주세요.

### 소스코드
```sql
SELECT ANIMAL_TYPE, coalesce(NAME, "No name"), SEX_UPON_INTAKE FROM ANIMAL_INS
```

### 해설
`coalesce` 함수를 사용하여 NAME이 NULL일 경우 No name을 출력하도록 수정한다.
