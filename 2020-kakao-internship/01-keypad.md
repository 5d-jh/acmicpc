## 2020 카카오 인턴십 - 키패드 누르기
### 소스코드
```py
def tup_dist(tup1, tup2):
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])
    

def solution(numbers, hand):
    answer = ''
    
    keypad = {
        '1': (0, 0), '2': (1, 0), '3': (2, 0),
        '4': (0, 1), '5': (1, 1), '6': (2, 1),
        '7': (0, 2), '8': (1, 2), '9': (2, 2),
        '*': (0, 3), '0': (1, 3), '#': (2, 3),
    }
    
    lpos = keypad['*']
    rpos = keypad['#']
    
    for n in numbers:
        n = str(n)
        
        if n in ['1', '4', '7']:
            answer += 'L'
            lpos = keypad[n]
        elif n in ['3', '6', '9']:
            answer += 'R'
            rpos = keypad[n]
        elif n in ['2', '5', '8', '0']:
            mpos = keypad[n]
            ldif = tup_dist(lpos, mpos)
            rdif = tup_dist(rpos, mpos)
            
            if ldif < rdif:
                answer += 'L'
                lpos = keypad[n]
            elif ldif > rdif:
                answer += 'R'
                rpos = keypad[n]
            else:
                if hand == 'left':
                    answer += 'L'
                    lpos = keypad[n]
                else:
                    answer += 'R'
                    rpos = keypad[n]
    
    return answer

```

### 해설
키패드의 위치를 미리 설정해둔 다음 들어오는 값에 따라 왼손 또는 오른손의 위치를 업데이트한다. 손가락은 상, 하, 좌, 우로만 이동 가능하기 때문에 거리 계산은 단순히 각 튜플의 x, y 값을 더했다. 시간 복잡도는 `O(n)`이다.