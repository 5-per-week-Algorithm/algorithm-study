def solution(s):
    answer = []
    s = list(s)
    num_of_zero = 0
    num_of_step = 0
    while s != '1':
        new_string = ''
        for i in range(len(s)):
            if s[i] == '0':
                num_of_zero += 1
                continue
            else:
                new_string += s[i]
        num_of_step += 1
        s = str(bin(len(new_string)))[2:]

    answer.append(num_of_step)
    answer.append(num_of_zero)

    return answer