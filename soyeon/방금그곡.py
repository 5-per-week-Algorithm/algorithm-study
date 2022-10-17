'''
https://school.programmers.co.kr/learn/courses/30/lessons/17683
계속 3개가 틀려서 왜 틀릴까 고민하던중
[반례]
"ABC" ["12:00,12:10,HELLO,ABC#ABC#ABC"] "HELLO"
내 로직 -> ABC#ABC#ABCA : (None)
ABC#이 있으면 None값을 반환하라고 했기에 답이 다르게 나왔다.

수정본
-> #이랑 같이 있는 건 소문자로 바꾸기
'''
# 원본(틀린 답)
import datetime as dt
musicinfos = ["12:00,12:10,HELLO,ABC#ABC#ABC"]
m = "ABC"
def solution(m, musicinfos):
    answer = []
    for music in musicinfos:
        list_ = music.split(',')
        start = dt.datetime.strptime(list_[0], "%H:%M")
        end = dt.datetime.strptime(list_[1], "%H:%M")
        n = int((end-start).seconds/60)
        tmp = len(list_[3]) - list_[3].count('#')
        
        몫 = int(n / tmp)
        나머지 = int(n % tmp)
        ans = ""
        
        for i in range(몫) :
            ans += list_[3]
        # 나머지 계산
        i = 0
        cnt = 0
        while True:
            if cnt == 나머지:
                break
            ans += list_[3][i]
            i += 1
            if list_[3][i] != '#':
                cnt += 1
        if list_[3][i] == '#':
            ans += '#'
        #print(ans)

        tmp_m = m+"#"
        if m in ans and tmp_m not in ans:
            answer.append([list_[2],n])
    
    if answer == []:
        return "(None)"
    answer.sort(key = lambda x: x[1], reverse=True)
    return answer[0][0]
#print(solution(m,musicinfos))

# 수정본(맞는 답)
import datetime as dt
musicinfos = ["03:00,03:08,FOO,CC#B"]
m = "CC#BCC#BCC#"
def solution(m, musicinfos):
    answer = []
    tmp = []
    for li in m:
        if li == '#' :
            tmp.append(chr(ord(tmp.pop()) + 32))
        else:
            tmp.append(li)
    new_m = ''.join(tmp)
    print(new_m)
    for music in musicinfos:
        list_ = music.split(',')
        start = dt.datetime.strptime(list_[0], "%H:%M")
        end = dt.datetime.strptime(list_[1], "%H:%M")
        n = int((end-start).seconds/60)
        tmp = []
        for li in list_[3]:
            if li == '#' :
                tmp.append(chr(ord(tmp.pop()) + 32))
            else:
                tmp.append(li)
        new_tmp = ''.join(tmp)
        몫 = int(n / len(new_tmp))
        나머지 = int(n % len(new_tmp))
        ans = ""
        for i in range(몫) :
            ans += new_tmp
        ans += new_tmp[:나머지]
        print(ans)
        if new_m in ans:
            answer.append([list_[2],n])
    if answer == [] :
        return "(None)"
    answer.sort(key=lambda x: x[1], reverse=True)
    return answer[0][0]

print(solution(m,musicinfos))


# 수정본(효율성 증가)
import datetime as dt
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
m = "ABC"
def changeTomin(str):
    return str.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g')
def solution(m, musicinfos):
    new_m = changeTomin(m)
    final = [0,'(None)']
    for info in musicinfos:
        list_ = info.split(',')
        new_music = changeTomin(list_[3])
        min = (int(list_[1][:2]) - int(list_[0][:2])) *60 + int(list_[1][3:5]) - int(list_[0][3:5])
        몫 = int(min / len(new_music))
        나머지 = int(min % len(new_music))
        ans = ""
        for j in range(몫):
            ans += new_music
        ans += new_music[:나머지]
        print(ans)
        if new_m in ans and final[0] < min:
            final = [min, list_[2]]
    return final[1]


print(solution(m,musicinfos))
    