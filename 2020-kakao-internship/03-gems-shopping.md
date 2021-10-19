## 2020 카카오 인턴십 - 보석 쇼핑
### 소스코드(효율성 탈락)
```py
import math

def solution(gems):
    num_kinds = len(set(gems))
    
    lpivot = 0
    rpivot = 0
    selected_kinds = len(set(gems[lpivot:rpivot]))
    minimum_range_size = math.inf
    lpivot_result = lpivot
    rpivot_result = rpivot
    
    for _ in range(len(gems)):
        while selected_kinds != num_kinds and rpivot < len(gems):
            rpivot += 1
            selected_kinds = len(set(gems[lpivot:rpivot]))

        while selected_kinds == num_kinds and lpivot <= rpivot:
            selected_kinds = len(set(gems[lpivot:rpivot]))
            lpivot += 1
            
            if selected_kinds != num_kinds and rpivot - lpivot < minimum_range_size:
                minimum_range_size = rpivot - lpivot
                lpivot_result = lpivot - 1
                rpivot_result = rpivot
                break
    
    if lpivot == rpivot:
        return [1, 1]
    
    return [lpivot_result, rpivot_result]
```
#### 해설
1. 모든 종류의 보석이 선택될 때까지 오른쪽 피벗을 1씩 증가시긴다.
2. 1이 종료되면 모든 종류의 보석이 선택되지 않을때까지 왼쪽 피벗을 1씩 증가시킨다.
3. 1이 종료되면 모든 종류의 보석이 선택되지 않았을 때, 선택 영역이 최소인지 확인하고 맞다면 갱신한다.
4. `len(gems)`만큼 위 과정을 반복한다.


### 소스코드(통과)
```py
import math

def solution(gems):
    num_kinds = len(set(gems))
    
    counts = {}
    
    lpivot = 0
    rpivot = 0
    
    minimum_range = math.inf
    lpivot_result = lpivot
    rpivot_result = rpivot
    
    while True:
        # 모든 종류의 보석을 포함하고 있는 경우
        if len(counts.keys()) == num_kinds:
            counts[gems[lpivot]] -= 1
            if counts[gems[lpivot]] <= 0:
                del counts[gems[lpivot]]
                
            # 가장 작은 선택 범위인 경우
            if rpivot - lpivot < minimum_range:
                minimum_range = rpivot - lpivot
                rpivot_result = rpivot
                lpivot_result = lpivot
            
            lpivot += 1
            
        # 더 이상 최적의 결과가 없는 경우
        elif len(gems) <= rpivot:
            break
            
        else:
            if gems[rpivot] not in counts:
                counts[gems[rpivot]] = 0
            
            counts[gems[rpivot]] += 1
            rpivot += 1
            
    
    if lpivot == rpivot:
        return [1, 1]
    
    return [lpivot_result + 1, rpivot_result]
```
#### 해설
기존과의 차이점
* 매번 set을 생성하여 종류 수를 세는 대신 map 기반으로 빈도수를 셋다. 
* 단순히 `gems`의 길이만큼 반복하는 대신, 더 이상 최적의 결과가 없는 경우를 고려하여 필요 없는 반복을 줄였다.

#### 참고
https://jujubebat.github.io/ps/pro67258/
