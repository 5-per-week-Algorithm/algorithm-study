from distutils.command.sdist import sdist

def convert(num, n):
    li = "0123456789ABCDEF"
    
    d,m = divmod(num,n)

    if d == 0:
        return li[m]
    else:
        return convert(d, n) + li[m]

def solution(n, t, m, p):
    answer = ""

    if p == m:
        p = 0
    num = 0
    order = 1

    while t > 0:
        numStr = convert(num, n)
        for c in numStr:
            if order == p:
                answer += c
                t -= 1
                if t <= 0:
                    break
            order = (order + 1) % m
        num += 1
    return answer



print(solution(16,16,2,2))