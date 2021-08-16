n = int(input())

cases = [1, 2, 4, 7]

for _ in range(n):
    num = int(input())
    
    while len(cases) < num:
        cases.append(sum(cases[-3:]))

    print(cases[num-1])
