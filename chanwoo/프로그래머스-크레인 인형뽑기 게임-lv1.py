def solution(board, moves):
    answer = 0
    stack = [-1]

    for move in moves:
        prevAnswer = answer
        for i in range(len(board)):
            if not board[i][move - 1] == 0:
                doll = board[i][move - 1]
                board[i][move - 1] = 0
                if stack[-1] == doll:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(doll)
                break
                
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))