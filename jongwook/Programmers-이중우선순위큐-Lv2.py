def solution(operations):
    answer = [0, 0]
    numbers = []
    for op in operations:
        op = op.split()
        if op[0] == 'I':
            numbers.append(int(op[1]))
            numbers.sort()
        if op[0] == 'D' and len(numbers) != 0:
            if op[1] == '1':
                numbers.pop(-1)
            if op[1] == '-1' and len(numbers) != 0:
                numbers.pop(0)

    if len(numbers) != 0:
        answer[1] = numbers[0]
        answer[0] = numbers[-1]

    return answer