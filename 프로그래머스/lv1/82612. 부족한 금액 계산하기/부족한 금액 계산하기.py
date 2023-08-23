def solution(price, money, count):
    for i in range(1, count + 1):
        money -= i * price
    return money * -1 if money < 0 else 0