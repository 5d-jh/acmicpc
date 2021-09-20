from typing import List


def solve(stairs: List[int]):
    step_history = []
    if len(stairs) == 1:
        return stairs[0]
    elif len(stairs) == 2:
        return max(stairs[1], stairs[1] + stairs[0])
    elif len(stairs) == 3:
        max(stairs[2] + stairs[0], stairs[2] + stairs[1])

    step_history.append(stairs[0])
    step_history.append(max(stairs[1], stairs[1] + stairs[0]))
    step_history.append(max(stairs[2] + stairs[0], stairs[2] + stairs[1]))

    for i in range(3, len(stairs)):
        step_history.append(max(stairs[i] + step_history[i - 2], stairs[i] + stairs[i - 1] + step_history[i - 3]))

    return step_history[-1]



N = int(input())

stairs = []

for _ in range(N):
    stairs.append(int(input()))


print(solve(stairs))
