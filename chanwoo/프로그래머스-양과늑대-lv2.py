def solution(info, edges):
    
    visited = [0 for _ in range(len(info))]
    visited[0] = 1
    maxSheep = 0
    def dfs(sheep, wolf):
        nonlocal maxSheep
        if sheep <= wolf:
            return

        for edge in edges:
            p = edge[0]
            c = edge[1]
            if visited[p] and not visited[c]:
                maxSheep = max(sheep + (info[c]^1), maxSheep)
                visited[c] = 1
                dfs(sheep+ (info[c]^1), wolf + info[c])
                visited[c] = 0
        
    dfs(info[0]^1, info[0])
    
    return maxSheep

print(solution([0,0,1,1,1,0,1,0,1,0,1,1],[[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))