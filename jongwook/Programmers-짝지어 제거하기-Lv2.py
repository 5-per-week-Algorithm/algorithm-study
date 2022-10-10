def solution(s):
    answer = -1

    if len(s) % 2:
        return 0
    else:
        stack = [s[0]]
        for i in s[1:]:
            if len(stack) > 0 and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    return 0 if len(stack) else 1