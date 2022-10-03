import collections
from itertools import combinations

def solution(orders, course):
    result = []
    for size in course:
        order_menus = []
        for order in orders:
            if len(order) >= size: pass
            order_menus += combinations(sorted(order), size)
        most_ordered = collections.Counter(order_menus).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
    return [ ''.join(v) for v in sorted(result) ]