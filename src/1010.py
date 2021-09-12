from functools import reduce
from operator import mul

def solve(N, M):
    a = reduce(mul, range(M, M - N, -1), 1)
    b = reduce(mul, range(1, N + 1), 1)
    return a // b


n = int(input())
for _ in range(n):
    N, M = map(int, input().split())

    print(solve(N, M))
