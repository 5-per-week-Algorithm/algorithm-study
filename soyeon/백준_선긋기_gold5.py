'''
https://www.acmicpc.net/problem/2170
선긋기.
문제 제대로 안읽어서 한번 틀림
스위핑 알고리즘 적용:

'''

import sys
N = int(input())
dots = []
answer = []
for i in range(N):
    x,y = map(int,sys.stdin.readline().strip().split())
    dots.append([x,y])
dots.sort(key=lambda x : x[1], reverse=True)
print(dots)
answer.append(dots[0])
tot = 0
for x1,y1 in dots:
    flag = 0
    for idx,an in enumerate(answer):
        x2,y2 = an
        if y1 >= x2:
            answer[idx][0] = min(answer[idx][0], x1)
            flag = 1
            break
    if flag == 0:
        answer.append([x1,y1])
for x,y in answer:
    tot += (y-x)
print(tot)

# 개선된 코드
import sys
N = int(input())
dots = []
answer = []
for i in range(N):
    x,y = map(int,sys.stdin.readline().strip().split())
    dots.append([x,y])
dots.sort()
#print(dots)

minMax = dots[0]
tot = 0
for x1,y1 in dots:
    #print(minMax)
    x2,y2 = minMax
    if y2 >= x1:
        minMax[1] = max(minMax[1],y1)
    else:
        tot += (minMax[1] - minMax[0])
        minMax = [x1,y1]
print(tot + (minMax[1] - minMax[0]))
