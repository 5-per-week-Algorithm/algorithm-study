def solution(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        num1 = 0
        num2 = 1
        for i in range(2,n+1):
            num3 = (num1 + num2) % 1234567
            num1 = num2
            num2 = num3
        return num3