'''
공통인 k개의 문자를 찾는 것이 목표
https://www.acmicpc.net/problem/1062
'''
import sys
from itertools import combinations
N,K = map(int,sys.stdin.readline().strip().split())
list_ = []
K -= 5
for i in range(N):
    input_ = set(input())
    input_ -= {'a','n','t','i','c'}
    if len(input_) <= K :
        tmp = 0
        for in_ in input_:
            tmp |= 1<<(ord(in_)-ord('a'))
        list_.append(tmp)
if K < 0:
    print(0)
    exit(0)
answer = []
alphabet = set("bdefghjklmopqrsuvwxyz")
bit = [1<<(ord(i)-ord('a')) for i in alphabet]
max_ = 0
for combination in combinations(bit,K):
    result = sum(combination)
    #print(result)
    tmp = 0
    for li in list_:
        if result & li == li:
            tmp += 1
    max_ = max(max_,tmp)
print(max_)




    