import sys

def bfs(a,b,list_):
    queue = [a]
    visited = [0 for _ in range(len(list_))]
    while queue:
        c = queue.pop(0)
        if c == b:
            return True
        visited[c] = 1
        for idx,li in enumerate(list_[c]):
            if li == 1 and visited[idx] == 0:
                queue.append(idx)
    return False

N = int(input())
M = int(input())
list_ = [[0]*N for _ in range(N)]
for i in range(N):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    for j in range(len(tmp)):
        list_[i][j] = tmp[j]
plan = list(map(int,sys.stdin.readline().strip().split()))
flag = 0
for p in range(len(plan)-1):
    if bfs(plan[p]-1,plan[p+1]-1,list_) == False:
        print("NO")
        flag = 1
        break
if flag == 0:
    print("YES")


        
