## 프로그래머스 위클리 챌린지 1주차 - 부족한 금액 계산하기 

https://programmers.co.kr/learn/courses/30/lessons/82612
### 소스코드
```py
def solution(price, money, count):
    sum = 0
    
    for c in range(count + 1)[1:]:
        sum += price * c

    if money < sum:
        return sum - money
    else:
        return 0
```

### 해설
`count`만큼 반복하여 필요한 금액을 계산하고, 요구 사항에 따라 결과값을 리턴한다. 시간 복잡도는 `O(n)`.

### 더 나은 방법
등비수열의 합 공식을 사용하면 `O(1)`로 해결할 수 있다.
