import itertools
from collections import defaultdict

def solution(orders, course):

    dict = defaultdict(int)

    for order in orders:
        for i in range(2,len(order)+1):
            li = list(itertools.combinations(order, i))
            for tup in li:
                dict["".join(sorted(tup))] += 1

    maxCounts = [0]*11
    maxCourses = [[] for i in range(11)]

    for c,count in dict.items():
        if maxCounts[len(c)] < count:
            maxCourses[len(c)] = [c]
            maxCounts[len(c)] = count
        elif maxCounts[len(c)] == count:
            maxCourses[len(c)].append(c)

    answer = [] 
    for n in course:
        if maxCounts[n] >= 2:
            answer.extend(maxCourses[n])
    
    answer.sort()
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))