from collections import deque


def solve(N):
    dq = deque(range(1, N + 1))
    
    while 1 < len(dq):
        dq.popleft()
        dq.append(dq.popleft())
    
    result = dq.popleft()
    return result


print(solve(int(input())))
