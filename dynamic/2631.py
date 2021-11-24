from typing import List


def solve(kids: List):
    lens = [1] * len(kids)

    for i, kid in enumerate(kids):
        for j in range(i):
            if kids[j] < kid:
                lens[i] = max(lens[i], lens[j] + 1)

    return len(kids) - max(lens)


N = int(input())
kids = []
for _ in range(N):
    kids.append(int(input()))

print(solve(kids))
