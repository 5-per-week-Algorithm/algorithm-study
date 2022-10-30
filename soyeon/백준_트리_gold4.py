'''
https://www.acmicpc.net/problem/4803
꼭 다시 풀어볼 문제.
'''
import sys
input = sys.stdin.readline

def dfs(start):
    visited[start] = True
    for n in graph[start]:
        if visited[n]:
            return False
        if not dfs(n):
            return False
    return True

'''
tc = 0
while True:
    tc += 1
    N, M = map(int, input().split())
    if [N, M] == [0, 0]: 
        break
    graph = [[] for _ in range(N+1)] 
    visited = [False] * (N+1) # 방문 여부
    for _ in range(M):
        a, b = map(int, input().split())
        if a>b: a,b = b,a
        graph[a].append(b) 
    #print(graph)
    cnt = 0 # 트리의 개수
    for v in range(1, N+1):
        if not visited[v]: # 방문하지 않은 경우만 DFS 수행
            if dfs(v):
                cnt += 1 # 사이클이 없는 경우 트리 개수 증가
    if cnt == 0:
        print("Case {}: No trees.".format(tc))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(tc))
    else:
        print("Case {}: A forest of {} trees.".format(tc, cnt))
'''
# 
tc = 0
while True:
    tc += 1
    n, m = map(int,sys.stdin.readline().strip().split())
    if [n,m] == [0,0]: break
    list_ = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for i in range(m):
        a , b = map(int,sys.stdin.readline().strip().split())
        if a > b : a,b = b,a
        list_[a].append(b)
    cnt = 0
    for i in range(1,n+1):
        if visited[i] == 0:
            visited[i] = 1
            queue = [i]
            flag = 0
            while queue:
                start = queue.pop(0)
                for j in list_[start]:
                    if visited[j] == 1:
                        flag = 1
                        break
                    visited[j] = 1
                    queue.append(j)
            if flag == 0:
                cnt += 1
    if cnt == 0:
        print("Case {}: No trees.".format(tc))
    elif cnt == 1:
        print("Case {}: There is one tree.".format(tc))
    else:
        print("Case {}: A forest of {} trees.".format(tc, cnt))
