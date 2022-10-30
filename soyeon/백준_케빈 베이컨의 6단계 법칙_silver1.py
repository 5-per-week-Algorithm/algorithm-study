'''
https://www.acmicpc.net/problem/1389
단순 bfs문제. 별 어려움 없이 풀었다.
'''
import sys
N, M = map(int,sys.stdin.readline().strip().split())
friends = [[] for _ in range(N)]
answer = 0
def bfs(start, visited):
    tot = 0
    queue = [[start, 0]]
    while queue:
        n,rtmp = queue.pop(0)
        if visited[n] == 1:
            continue
        tot += rtmp
        visited[n] = 1
        for i in friends[n]:
            if visited[i] == 0:
                queue.append([i,rtmp+1])
    return tot
        




for i in range(M):
    a,b = map(int,sys.stdin.readline().strip().split())
    a -= 1
    b -= 1
    friends[a].append(b)
    friends[b].append(a)
#print(friends)
min_ = 10*10
answer = 0
for i in range(N):
    visited = [0 for _ in range(N)]
    an = bfs(i, visited)
    if min_ > an:
        min_ = an
        answer = i
print(answer+1)
