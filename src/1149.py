def solve(costs):
    pr, pg, pb = costs[0]

    for r, g, b in costs[1:]:
        npr = min(r + pg, r + pb)
        npg = min(g + pr, g + pb)
        npb = min(b + pr, b + pg)
        pr = npr
        pg = npg
        pb = npb

    return min(pr, pg, pb)


N = int(input())
costs = []
for _ in range(N):
    rgb = map(int, input().split())
    costs.append(rgb)

print(solve(costs))
