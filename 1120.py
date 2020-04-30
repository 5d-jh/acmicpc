def solution(a, b):
    str_len_diff = len(b) - len(a)
    minimum = len(b)
    for i in range(str_len_diff + 1):
        left = b[0:str_len_diff - i]
        right = b[-i:] if i > 0 else ''
        tmp_string = left + a + right

        #두 문자열의 차이 구하기
        diff_sum = sum(map(lambda e: e[0] != e[1], zip(tmp_string, b)))
        if diff_sum < minimum:
            minimum = diff_sum
    
    print(minimum)

a, b = input().split()
solution(a, b)