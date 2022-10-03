#
# Created by frank on 22. 9. 28.
#
def solution(s):
    s = list(map(int, s.split()))
    print('"{} {}"'.format(min(s), max(s)))
    answer = str(min(s)) + " " + str(max(s))
    return answer