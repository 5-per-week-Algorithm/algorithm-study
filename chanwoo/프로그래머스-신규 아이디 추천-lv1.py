import string

def solution(new_id):

    s = new_id
    #1단계
    s = new_id.lower()
    #2단계
    rule = list(string.ascii_lowercase + string.digits + "-_.")
    new_s = s
    for c in s:
        if not c in rule:
            new_s =  new_s.replace(c, "")
    s = new_s
        
    #3
    for i in reversed(range(2,1001)):
        s = s.replace("."*i, ".")

    #4
    if not s == "" and s[0] == ".":
        s = s[1:]
    if not s == "" and s[-1] == ".":
        s = s[:len(s)-1]
    
    #5
    if s == "":
        s = "a"

    #6
    if len(s) >= 16:
        s = s[:15]
        if s[-1] == ".":
            s = s[:len(s)-1]
    #7
    while len(s) <= 2:
        s += s[-1]

    return s

print(solution(	"abcdefghijklmn.p"))