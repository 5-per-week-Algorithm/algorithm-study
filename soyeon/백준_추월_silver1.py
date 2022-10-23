'''
https://www.acmicpc.net/problem/2002
이게 왜 dp문제일까~?
'''
N = int(input())
start = []
end = []

for i in range(N):
    start.append(input())

for i in range(N):
    end.append(input())
e_idx = 0
tot = N
for s in start:
    for i in range(e_idx,len(end)):
        if s == end[i]: 
            tot -= 1
            e_idx = i
            break
print(tot)