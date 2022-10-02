
import copy
routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
routes.sort(key=lambda x:x[1])
num = 0
print(routes)
while routes:
    start = routes[0][1]
    num += 1
    for s,e in routes[:]:
        if s <= start:
            routes.remove([s,e])
print(num)
