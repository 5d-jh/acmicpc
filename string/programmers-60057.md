## 프로그래머스 문자열 압축
https://programmers.co.kr/learn/courses/30/lessons/60057

> 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.


### 소스코드
```py
def solution(s):
    global_result = s
    
    for substr_len in range(1, len(s) + 1):
        prev_str = s[0:substr_len]
        consec_stack = 1
        partial_result = ''
        
        for i in range(substr_len, len(s), substr_len):
            curr_str = s[i:i + substr_len]
                        
            if prev_str == curr_str:
                consec_stack += 1
            elif 1 < consec_stack:
                partial_result += str(consec_stack) + prev_str
                consec_stack = 1
            else:
                partial_result += prev_str
                consec_stack = 1
            
            prev_str = curr_str
        
        if 1 < consec_stack:
            partial_result += str(consec_stack) + prev_str
        else:
            partial_result += prev_str
        
        if len(partial_result) < len(global_result):
            global_result = partial_result
            
    
    return len(global_result)
```

### 해설
문자열을 길이별(`substr_len`)로 잘라가며 압축 결과를 구해, 가장 최소 값을 구하는 문제다.

`substr_len` 길이를 점점 늘려가며 문자열 압축을 시도하기 때문에 시간 복잡도는 `O(n^2)`로 예상된다.
