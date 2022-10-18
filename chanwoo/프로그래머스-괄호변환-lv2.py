

def makeCorrect(s):
    if s == "":
        return ""

    li = []
    u = ""
    v = ""

    perfect = True
    inputChar = "("

    if s[0] == ")":
        inputChar = ")"
        perfect = False

    for i,c in enumerate(s):

        if c == inputChar:
            li.append(inputChar)
        else:   
            li.pop()        
            if len(li) == 0:
                u = s[:i+1]
                v = s[i+1:]
                break
                
        
    if perfect:
        return u + makeCorrect(v)
    
    u = u[1:len(u)-1]
    newU = ""
    for c in u:
        if c == "(":
            newU +=  ")"
        else:
            newU += "("

    return '(' + makeCorrect(v) + ')' + newU
    

def solution(p):
    answer = makeCorrect(p)
    return answer


print(solution("()))((()"))