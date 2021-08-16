kids = [-1]
lisset = [[-1]]

def get_lis(lst):
    for s in lst:
        candidate = []

        for e in lst:
            if e > s:
                candidate.append()


N = int(input())

for _ in range(N):
    kid = int(input())
    kids.append(kid)
    get_lis()
    print(lisset)


