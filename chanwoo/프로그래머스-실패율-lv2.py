from collections import Counter
def solution(N, stages):
    
    c = Counter(stages)

    accumulate = 0
    if N+1 in c:
       accumulate = c[N+1]
       del(c[N+1])

    answersDict = { i:0 for i in range(1,N+1)}
    for stage, count in sorted(list(c.items()),key = lambda x : x[0], reverse= True):
        accumulate += count
        answersDict[stage] = count / accumulate

    return sorted(answersDict, key = lambda x : answersDict[x] , reverse=True)


print(solution(4,[4,4,4,4,4]))