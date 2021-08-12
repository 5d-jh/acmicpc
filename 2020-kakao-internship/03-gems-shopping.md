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
