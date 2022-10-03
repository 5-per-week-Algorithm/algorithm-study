def solution(s):
    answer = True
    check = []
    for p in range(len(s)):
        if s[p] == '(':
            check.append('a')
        elif s[p] == ')':
            if len(check) == 0:
                return False
            check.pop()

    if len(check) == 0:
        return answer
    else:
        return False