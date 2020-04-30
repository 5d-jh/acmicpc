def solution(strings, packages, singles):
    pack_min = min(packages)
    sing_min = min(singles)

    price_packages = (strings // 6) * pack_min
    price_singles = (strings % 6) * sing_min

    if price_singles > pack_min:
        price_singles = pack_min

    print(min((strings // 6 + 1) * pack_min, price_packages + price_singles, sing_min * strings))
    

n, m = map(int, input().split())
packages = []
singles = []
for _ in range(m):
    package, single = tuple(map(int, input().split()))
    packages.append(package)
    singles.append(single)

solution(n, packages, singles)