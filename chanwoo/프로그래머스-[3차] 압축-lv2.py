from string import ascii_uppercase

def solution(msg):

    answer = []
    li = list(ascii_uppercase)
    li.insert(0,"")
    i = 0
    while i < len(msg):
        for j in reversed(range(1,len(li))):
            if msg[i:].startswith(li[j]):
                answer.append(j)
                if i + len(li[j]) < len(msg):
                    li.append(li[j] + msg[i+len(li[j])])
                    i += len(li[j])
                    break
                elif i + len(li[j]) == len(msg):
                    return answer

    return answer

print(solution("TOBEORNOTTOBEORTOBEORNOT"))
                    
                 