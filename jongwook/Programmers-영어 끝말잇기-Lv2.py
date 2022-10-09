4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
def solution(n, words):
    answer = []

    check = []
    count = 1
    turn = 1
    last_letter = words[0][0]
    first_letter = words[0][0]
    for word in words:
        if count == n + 1:
            count = 1
            turn += 1
        if word in check:
            answer.append(count)
            answer.append(turn)
            return answer
        else:
            if word[0] == last_letter:
                check.append(word)
                last_letter = word[-1]
            else :
                answer.append(count)
                answer.append(turn)
                return answer

        count += 1

    return [0,0]