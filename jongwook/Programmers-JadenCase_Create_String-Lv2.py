#
# Created by frank on 22. 9. 28.
#
def solution(s):
    s = list(s)
    is_first = True

    for i in range(len(s)):
        if is_first and s[i].isalpha() and s[i].islower():
            s[i] = s[i].upper()
            is_first = False
        elif is_first != True and s[i].isupper():
                s[i] = s[i].lower()
        if s[i] == " ":
            is_first = True
        else:
            is_first = False

        answer = ''.join(s)
    return answer