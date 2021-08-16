n = int(input())
p = list(map(int, input().split()))

p.sort(reverse=True)

result = 0
for i in range(n):
    result += (i + 1) * p[i]

print(result)