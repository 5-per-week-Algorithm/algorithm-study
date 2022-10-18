def getDist(n, handNum,mDict):
    fy,fx = mDict[handNum]
    ty,tx = mDict[n]
    
    return abs(fy-ty) + abs(fx-tx) 

def solution(numbers, hand):
    answer = ''

    ll = "*"
    lr = "#"

    m = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ["*",0,"#"]
    ]
    
    mDict = {}

    for i in range(len(m)):
        for j in range(len(m[0])):
            mDict[m[i][j]] = (i,j)

    for n in numbers:
        if n in [1,4,7]:
            answer += "L"
            ll = n
        elif n in [3,6,9]:
            answer += "R"
            lr = n
        else:
            if getDist(n,ll, mDict) > getDist(n,lr,mDict):
                answer += "R"
                lr = n
            elif getDist(n,ll, mDict) < getDist(n,lr,mDict):
                answer += "L"
                ll = n
            else:
                if hand == "right":
                    answer += "R"
                    lr = n
                else:
                    answer += "L"
                    ll = n
            
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))