## 프로그래머스 올바른 괄호
https://programmers.co.kr/learn/courses/30/lessons/12909

> '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 하고, 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.


### 소스코드
```py
def solution(s):
    result = 0
    for c in s:
        if c == '(':
            result += 1
        else:
            result -= 1
        
        if result < 0:
            return False
    
    return result == 0
```

### 해설
문자열에서 '('가 나오면 `result`를 1 증가시키고, 아니라면 1 감소시킨다.

만약 `result`가 0보다 작다면 False를 리턴한다.

반복문을 완료했다면 `result`가 0인지 검사한다. (1 이상이라면 괄호가 열린채로 닫히지 않은 상태다)
