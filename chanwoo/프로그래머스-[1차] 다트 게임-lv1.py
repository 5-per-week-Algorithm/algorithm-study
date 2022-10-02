def cal(round):
    score = 0
    numList = list("0123456789")
    
    if not round[1] in numList:
        num = int(round[0])
        round = round[1:]
    else:
        num = int(round[:2])
        round = round[2:]

    bonus = round[0]
    
    op = round[-1] if len(round) == 2 else -1        

    if bonus == "S":
        score += num
    elif bonus == "D":
        score += num**2
    else:
        score += num**3
    
    if op == "#":
        score = -score
    elif op == "*":
        score *= 2

    return (score,op)

def solution(dartResult):
    answer = 0

    numList = list("0123456789")

    beforeScore = 0

    for (i,c) in enumerate(list(dartResult)):
        if not c in numList:
            continue
        if dartResult[i-1] in numList:
            continue

        e = i+1

        if c == '1' and dartResult[i+1] == '0':
            e += 1

        if e+1 < len(dartResult) and (dartResult[e+1] == "*" or dartResult[e+1] == "#"):
               e += 1 

        round = dartResult[i:e+1]

        score, op = cal(round)

        if op == "*":
            answer += beforeScore
        answer += score
        beforeScore = score

    return answer


print(solution("1D2S#10S"))