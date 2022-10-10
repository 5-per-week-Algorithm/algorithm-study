from numpy import kaiser




def solution(m, n, board):

    dir = [(0,0),(1,0),(0,1),(1,1)]
    for i in range(m):
        board[i] = list(board[i])
    
    answer = 0
    count = 0

    while True:
        count = 0
        boom = [[0 for _ in range(n)] for __ in range(m)] 
        for i in range(m-1):
            for j in range(n-1):
                c = board[i][j]
                for ny,nx in dir:
                    if 0 <= i+ny < m and 0 <= j+nx < n:
                        if not c == board[i+ny][j+nx] or c == " ":
                            c = " "
                            break
                if not c == " ":
                    for ny,nx in dir:
                        if 0 <= i+ny < m and 0 <= j+nx < n:
                            if boom[i+ny][j+nx] == 0:
                                boom[i+ny][j+nx] = 1
                                count += 1

        if count == 0:
            break
        
        answer += count
        for i in range(m):
            for j in range(n):
                if boom[i][j] == 1:
                    for k in reversed(range(0,i)):
                        board[k+1][j] = board[k][j]
                    board[0][j] = " "
    return answer


print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
