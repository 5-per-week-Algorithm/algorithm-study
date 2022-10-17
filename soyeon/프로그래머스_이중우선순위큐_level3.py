import heapq as h
operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
max_queue = []
min_queue = []
for op in operations :
    if op[0] == "I":
        h.heappush(max_queue,-int(op[2:]))
        h.heappush(min_queue,int(op[2:]))
    elif op == "D 1":
        if max_queue :
            n = h.heappop(max_queue)
            min_queue.remove(-n)
    else:
        if min_queue :
            n = h.heappop(min_queue)
            max_queue.remove(-n)
if max_queue:
    max_ = -h.heappop(max_queue)
    min_ = h.heappop(min_queue)
    print([max_,min_])
else:
    [0,0]