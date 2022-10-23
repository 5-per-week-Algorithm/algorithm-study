'''
https://www.acmicpc.net/problem/10799
'''
input = input()
new = input.replace('()','.')
#print(new)
cnt = 0
tot = 0
for n in new:
    if n == '(':
        cnt += 1
    elif n == ')':
        cnt -= 1
        tot += 1
    elif n == '.':
        tot += cnt
print(tot)