U = [1,0]
D = [-1,0]
R = [0,1]
L = [0,-1]
dirs = "LULLLLLLU"
visited = [[0]*10 for _ in range(10)]
answer = 1
def solution(dirs):
    global visited
    global answer
    s_x = 5
    s_y = 5
    for dir in dirs:
        if dir == 'U':
            n_x = s_x + U[1]
            n_y = s_y + U[0]
        elif dir == 'L':
            n_x = s_x + L[1]
            n_y = s_y + L[0]
        elif dir == 'R':
            n_x = s_x + R[1]
            n_y = s_y + R[0]
        elif dir == 'D':
            n_x = s_x + D[1]
            n_y = s_y + D[0]
        if 0<=n_x<=10 and 0<=n_y<=10:
            s_x = n_x
            s_y = n_y
            print(s_x,s_y)
            visited[s_y][s_x] = visited[s_y][s_x] + 1
            if visited[s_y][s_x] == 1 : 
                answer += 1
solution(dirs)
print(visited)
print(answer)