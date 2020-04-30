n, k = input().split()
n, k = int(n), int(k)

coins = []
for _ in range(n):
    coins.append(int(input()))

coins.reverse()

result = 0

for coin in coins:
    if k // coin != 0:
        result += (k // coin)
        k -= coin * (k // coin)

print(result)