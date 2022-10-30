'''
https://www.acmicpc.net/problem/5002
뒤에 사람이 다른 성별인지만 구별하면 되는 케이스.
'''
from collections import deque

X = int(input())
input = deque(input())
tot = man = woman = 0
while input:
    cur = input.popleft()
    if cur == 'M':
        if abs(man + 1 - woman) <= X:
            man += 1
            tot += 1
        # 다음께 존재할 때
        elif input and abs(man + 1 - woman) > X:
            next = input.popleft()
            # 다른 성별이어야 함
            if next == 'W':
                if abs(woman + 1 - man) <= X:
                    input.appendleft(cur)
                    woman += 1
                    tot += 1
                else:
                    break
            else:
                break
    else:
        if abs(woman + 1 - man) <= X:
            woman += 1
            tot += 1
        elif input and abs(woman + 1 - man) > X:
            next = input.popleft()
            if next == 'M':
                if abs(man + 1 - woman) <= X:
                    input.appendleft(cur)
                    man += 1
                    tot += 1
                else:
                    break
            else:
                break
print(tot)
