from operator import concat
from functools import reduce

counts = {
    '-1': 0,
    '0': 0,
    '1': 0
}

matrix = []

def solve(x, y, chunk_size):
    if chunk_size == 0:
        return

    all_same = True
    prev_el = matrix[y][x]
    for row in matrix[y : y + chunk_size]:
        if not all_same:
            break

        for elem in row[x : x + chunk_size]:
            if prev_el != elem:
                all_same = False
                break
    
    
    if all_same:
        counts[prev_el] += 1
        return

    chunk_size //= 3
    
    solve(x, y, chunk_size)
    solve(x, y + chunk_size, chunk_size)
    solve(x, y + chunk_size * 2, chunk_size)

    solve(x + chunk_size, y, chunk_size)
    solve(x + chunk_size, y + chunk_size, chunk_size)
    solve(x + chunk_size, y + chunk_size * 2, chunk_size)

    solve(x + chunk_size * 2, y, chunk_size)
    solve(x + chunk_size * 2, y + chunk_size, chunk_size)
    solve(x + chunk_size * 2, y + chunk_size * 2, chunk_size)


N = int(input())

for _ in range(N):
    row = input().split(' ')
    matrix.append(row)

solve(0, 0, N)

print(counts['-1'])
print(counts['0'])
print(counts['1'])
