import sys
N = int(input())
parent = [[] for _ in range(N)]

def preorder(node, parent):
    print(chr(node+ord('A')),end='')
    if parent[node][0] >= 0:
        preorder(parent[node][0],parent)
    if parent[node][1] >= 0:
        preorder(parent[node][1],parent)

def inorder(node, parent):
    if parent[node][0] >= 0:
        inorder(parent[node][0],parent)
    print(chr(node+ord('A')),end='')
    if parent[node][1] >= 0:
        inorder(parent[node][1],parent)

def postorder(node, parent):
    if parent[node][0] >= 0:
        postorder(parent[node][0],parent)
    if parent[node][1] >= 0:
        postorder(parent[node][1],parent)
    print(chr(node+ord('A')),end='')
for i in range(N):
    p,l,r = sys.stdin.readline().strip().split()
    parent[ord(p)-ord('A')] = [ord(l)-ord('A'),ord(r)-ord('A')]
preorder(0,parent)
print()
inorder(0,parent)
print()
postorder(0,parent)