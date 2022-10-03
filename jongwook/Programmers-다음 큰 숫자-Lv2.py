def solution(n):
    answer = 0
    binary = str(bin(n))[2:]
    counter = binary.count('1')
    print(counter)
    while 1:
        n += 1
        if str(bin(n))[2:].count('1') == counter:
            return n
