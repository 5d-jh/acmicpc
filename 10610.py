def solution(n):
    nums = list(n)
    nums.sort(reverse=True)
    if nums[-1] == '0':
        nums.pop()
        if int(''.join(nums)) % 3 == 0:
            print(''.join(nums) + '0')
        else:
            print(-1)
    else:
        print(-1)

n = input()
solution(n)