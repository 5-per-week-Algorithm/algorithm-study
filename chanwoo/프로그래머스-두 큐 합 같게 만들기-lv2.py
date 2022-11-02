from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q1s = sum(queue1)
    q2 = deque(queue2)
    q2s = sum(queue2)

    max_count = (len(queue1)+len(queue2))*2
    count = 0
    while count <= max_count:
        if q1s < q2s:
            k = q2.popleft()
            q1.append(k)
            q1s += k
            q2s -= k
        elif q1s > q2s:
            k = q1.popleft()
            q2.append(k)
            q2s += k
            q1s -= k
        else:
            break
        count += 1
    if count > max_count:
        return -1
    else:
        return count

print(solution( [1, 1, 1, 1, 1], [1, 1, 1, 9, 1] ))