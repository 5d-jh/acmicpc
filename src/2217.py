def solution(ropes):
    ropes.sort(reverse=True)
    max = 0
    for i in range(len(ropes)): 
        tolerable = ropes[-1] * len(ropes)
        if tolerable > max:
            max = tolerable
        ropes.pop()
    print(max)

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
solution(ropes)