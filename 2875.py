def solution(n, m, k):
    team = int(n / 2) #원래 있어야할 팀 수
    if m < team:
        team = m

    #나가도 상관없는 사람수
    can_leave_n = n - team * 2
    can_leave_m = m - team

    if can_leave_n + can_leave_m >= k:
        print(team)
        return

    crucial = team * 3 #반드시 있어야 팀이 최대로 유지
    
    print((crucial + can_leave_m + can_leave_n - k) // 3)
    

n, m, k = list(map(int, input().split()))
solution(n, m, k)

"""
4 2 1 -> 1
10 1 1 -> 1
"""