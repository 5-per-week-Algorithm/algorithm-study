from collections import defaultdict;

def solution(survey, choices):
    
    s = "RTCFJMAN"
    dict = {}
    for c in s:
        dict[c] = 0

    for i in range(len(survey)):
        f,b = survey[i]
        score = abs(choices[i] - 4)    
        
        if choices[i] < 4:
            dict[f] += score
        else: 
            dict[b] += score
    answer = ''
    for i in range(0,8,2):
        if dict[s[i]] >= dict[s[i+1]]:
            answer += s[i]
        else:
            answer += s[i+1]
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))