def solve(n: int):
    history = [0] * max(2, n + 1)

    for i in range(2, n + 1):
        if i % 6 == 0:
            history[i] = min(history[i // 3] + 1, history[i // 2] + 1, history[i - 1] + 1)
        elif i % 3 == 0:
            history[i] = min(history[i // 3] + 1, history[i - 1] + 1)
        elif i % 2 == 0:
            history[i] = min(history[i // 2] + 1, history[i - 1] + 1)
        else:
            history[i] = history[i - 1] + 1
    
    return history[-1]


print(solve(int(input())))
