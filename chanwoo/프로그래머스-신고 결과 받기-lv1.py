from collections import defaultdict

def solution(id_list, report, k):
    
    answer = [0]* len(id_list)
    nameDict = { id_list[i]:i for i in range(len(id_list))}

    setDict = defaultdict(set)


    for i in range(len(report)):
        reporter, hacker = report[i].split()
  
        setDict[hacker].add(reporter)

    for hacker, reporters in setDict.items():

        if len(reporters) >= k:
            for reporter in reporters:
                index = nameDict[reporter]
                answer[index] += 1
    
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))