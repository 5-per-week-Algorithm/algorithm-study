def solution(arr):
    answer = 0
    current = arr[0]
    for item in arr:
        bigger = current if current > item else item
        while True:
            if bigger % current == 0 and bigger % item == 0:
                answer = bigger
                break
            bigger += 1
        current = answer

    return answer