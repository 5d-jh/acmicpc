def solve(T):
    if T == 0:
        return 0

    buttons = (300, 60, 10)
    counts = [0, 0, 0]
    dt = T

    for i, button in enumerate(buttons):
        if dt <= 0:
            break

        counts[i] = dt // button
        dt -= counts[i] * button

    if dt > 0:
        return -1
    
    return counts



T = int(input())
result = solve(T)
if result == -1 or result == 0:
    print(result)
else:
    A, B, C = result
    print(A, B, C)
