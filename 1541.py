def solution(s):
    s = s.split('-')
    sums = []
    for plus_s in s:
        nums = map(int, plus_s.split('+'))
        sums.append(sum(nums))
    
    if len(s) > 1:
        result = sums[0] -sum(sums[1:])
    else:
        result = sum(sums)
    
    print(result)
    
    
s = input()
solution(s)