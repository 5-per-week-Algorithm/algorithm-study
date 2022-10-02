from itertools import combinations_with_replacement

def calScore(info, lion):
    aScore = 0
    lScore = 0

    for i in range(len(info)):
        if info[i] < lion[i]:
            lScore += 10-i
        elif info[i] == 0:
            continue            
        else:
            aScore += 10-i

    return lScore - aScore 

def solution(n, info):
    
    
    maxScore = -float('inf')
    answer = []
    li = [ i for i in reversed(range(11))]
    for indexs in combinations_with_replacement(li, n):
        lion = [0] * 11
        for index in indexs:
            lion[index] += 1
        
        score = calScore(info, lion)
        if maxScore < score:
            answer = lion
            maxScore = score
        
    if maxScore <= 0:
        answer = [-1]
    print(maxScore)    
    return answer

print(solution(	9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))