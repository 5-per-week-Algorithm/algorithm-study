'''
bfs로 사용
icn -> sfo, atl 
    -> atl, icn
    -> sfo, sfo
    -> 
'''
import copy
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
visited = [0 for _ in range(len(tickets))]
answer = []
queue = ["ICN"]
def dfs(queue,visited,tmp):
    global answer
    start = queue.pop(0)
    flag = 0
    for idx, ticket in enumerate(tickets):
        a,b = ticket
        if a == start and visited[idx] == 0:
            queue.append(b)
            tmp.append(b)
            visited[idx] = 1
            dfs(queue,visited,tmp)
            visited[idx] = 0
            tmp.pop()
            flag = 1
    if flag == 0 and len(tmp) == len(tickets)+1:
        new_tmp = copy.deepcopy(tmp)
        answer.append(new_tmp)
        answer.sort()
dfs(queue,visited,["ICN"])
print(answer[0])

