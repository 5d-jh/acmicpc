def solution(price):
    monies = [500, 100, 50, 10, 5, 1]
    change = 1000 - price
    result = 0
    for money in monies:
        if change // money != 0:
            result += change // money
            change -= (change // money) * money
    print(result)


price = int(input())
solution(price)