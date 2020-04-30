def solution(times):
    times.sort(key=lambda e: e[0])

    last, length = times[0][1], 1

    for duration in times[1:]:
        start, end = duration
        if last <= start:
            last = end
            length += 1

    print(length)

n = int(input())

times = []
for _ in range(n):
    start, end = input().split()
    start, end = int(start), int(end)
    times.append((start, end))
solution(times)