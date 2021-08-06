def solve(n: int):
    lst = set([n])
    result = 1

    while 3 not in lst and 5 not in lst:
        newlst = set()

        for el in lst:
            if el > 5:
                newlst.add(el - 5)
            if el > 3:
                newlst.add(el - 3)

        if len(newlst) == 0:
            return -1

        del lst
    
        lst = newlst
        result += 1

    return result

n = int(input())
print(solve(n))
