from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    max_count = len(queue1)+len(queue2)
    count = 0
    while count <= max_count:
        if sum(q1) < sum(q2):
            q1.append(q2.popleft)
        elif sum(q1) > sum(q2):
            q2.append(q1.popleft)
        else:
            break
        count += 1
    if count == max_count:
        return -1
    else:
        return count

print(solution([3, 2, 7, 2],[4, 6, 5, 1]))