from pyparsing import java_style_comment


def solution(record):
    
    userDict = {}
    
    data = []

    for i, r in enumerate(record):
        rList = r.split()
        if len(rList) == 3:
            commend, id, name = rList
            userDict[id] = name
        else:
            commend, id = rList
        data.append([commend, id])

    answer = []

    for i in range(len(data)):
        if data[i][0] == "Enter":
            answer.append(userDict[data[i][1]] + "님이 들어왔습니다.")
        elif data[i][0] == "Leave":
            answer.append(userDict[data[i][1]] + "님이 나갔습니다.")
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
