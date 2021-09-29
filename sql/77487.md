## 프로그래머스 77487
https://programmers.co.kr/learn/courses/30/lessons/77487

> 이 서비스에서는 공간을 둘 이상 등록한 사람을 "헤비 유저"라고 부릅니다. 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회하는 SQL문을 작성해주세요.

### 소스코드
```sql
select A.ID, A.NAME, A.HOST_ID from PLACES as A where HOST_ID IN(
    select B.HOST_ID from PLACES as B group by (B.HOST_ID) having count(*) >= 2
)
```

### 해설
B의 `HOST_ID`를 기준으로 그룹화하여 각 그룹의 합이 2 이상인 `HOST_ID`를 찾는다. 그 다음 `IN`을 사용하여 `HOST_ID`에 따른 레코드들을 출력한다.
