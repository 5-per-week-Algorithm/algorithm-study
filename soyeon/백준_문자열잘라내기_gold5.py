import sys
R,C = map(int,sys.stdin.readline().strip().split())

list_ = []
for i in range(R):
    list_.append(input())

tot = ["" for _ in range(C)]
cnt = 0

for i, li in enumerate(list_[::-1]):
    flag = 0
    for idx, ele in enumerate(li):
        set_tot = set(tot)
        #print(tot[idx] + ele, set_tot)
        if tot[idx] + ele in set_tot:
            flag = 1
        tot[idx] = tot[idx] + ele
    if flag == 0:
        cnt = i
        break
print(R-cnt-1)
