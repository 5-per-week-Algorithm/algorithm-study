from math import ceil
def solution(n, words):

    round = 0
    dict = {}
    prevWord = words[0][0]
    for i in range(len(words)):

        if words[i] in dict or prevWord[len(prevWord)-1] != words[i][0]:
            p = (i+1)%n
            p = n if p == 0 else p
            return [p, ceil((i+1)/n)]
        
        dict[words[i]] = ""
        prevWord = words[i]

    return [0,0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))