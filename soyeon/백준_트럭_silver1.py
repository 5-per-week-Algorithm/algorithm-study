'''
https://www.acmicpc.net/problem/13335
한번에 트럭 group이 결정되는 것이 아니라 계속 이동하면서 뒤의 트럭이 붙을 수 있다는 사실을 생각하지 못했다.
진짜 트럭이 이동하는 것처럼 생각하기
'''
import sys
from collections import deque
n, w, L = map(int,sys.stdin.readline().strip().split())
weight = deque(map(int,sys.stdin.readline().strip().split()))
tmp = [0 for _ in range(w)]
time = 0
while tmp:
    tmp.pop(0)
    if weight:
        a = weight.popleft()
        if a + sum(tmp) <= L:
            tmp.append(a)
        else :
            tmp.append(0)
            weight.appendleft(a)
    time += 1
print(time)

