import copy
def preorder(sortY, sortX, answer):
    sortY1 = []
    sortY2 = []
    node = sortY[0]
    idx = sortX.index(node)

    for i in range(1,len(sortY)):
        if sortY[i][0] >= node[0]:
            sortY2.append(sortY[i])
        else:
            sortY1.append(sortY[i])
    
    answer.append(node)
    if len(sortY1) >= 1:
        preorder(sortY1, sortX[:idx], answer)
    if len(sortY2) >= 1:    
        preorder(sortY2, sortX[idx+1:], answer)
    return
    
    
def postorder(sortY, sortX, answer):
    sortY1 = []
    sortY2 = []
    node = sortY[0]
    idx = sortX.index(node)
    for i in range(1,len(sortY)):
        if sortY[i][0] > node[0]:
            sortY2.append(sortY[i])
        else:
            sortY1.append(sortY[i])
    if len(sortY1) >= 1:
        postorder(sortY1, sortX[:idx], answer)
    if len(sortY2) >= 1:
        postorder(sortY2, sortX[idx+1:], answer)
    answer.append(node)
    return
    
def solution(nodeinfo):
    for idx,node in enumerate(nodeinfo):
        node.append(idx)
    sortY = copy.deepcopy(nodeinfo)
    sortY.sort(key = lambda x: (-x[1], x[0]))
    sortX = copy.deepcopy(nodeinfo)
    sortX.sort(key = lambda x : x[0])
    print(sortY)
    print(sortX)
    answer = []
    preorder(sortY, sortX,answer)
    print(answer)
    answer = []
    postorder(sortY, sortX, [])
    print(answer)
    
    
 
    
solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])