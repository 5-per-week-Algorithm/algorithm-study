import string

def parse(s):

    head = ""
    num = ""
    tail = ""
    digit = list(string.digits)
    for i,c in enumerate(s):
        if c in digit: 
            if head == "":
                head = s[:i]
            if len(num) < 5:
                num += c
            else:
                tail = s[i:]
                break
        else:
            if not num == "":
                tail = s[i:]
                break
    return [head,num,tail]

def solution(files):

    li = []
    for s in files:
        p = parse(s)
        li.append(p)

    li = sorted(li,key= lambda x : (x[0].lower(),int(x[1])))  

    for i,sLi in enumerate(li):
        li[i] = ''.join(sLi)
    return li

print(solution(["F-5 Freedom Fighter", "F-05 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))