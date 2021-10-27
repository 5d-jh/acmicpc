N, M = map(int, input().split())

not_seen = set()
for _ in range(N):
    not_seen.add(input())

result = []
for _ in range(M):
    not_heard = input()
    if not_heard in not_seen:
        result.append(not_heard)

print(len(result))
for name in sorted(result):
    print(name)
