n = int(input())

def solution(n):
    if n < 0:
        return -1

    fives = n // 5
    threes = n // 3

    if n % 5 == 0:
        return fives
    elif n % 3 == 0:
        return threes
    else:
        return min(fives, threes) + solution(n - 5)


print(solution(n))
