

def canGo(place, y,x):
    
    if 0<=y<len(place) and 0 <=x<len(place[0]):
        if place[y][x] == "O" or place[y][x] == "P":
            return True

    return False


def isGood(place,d, dirNum,y,x):
    dirs = [(1,0), (0,1),(-1,0),(0,-1)]
    if d == 0:
        return True

    for i,dir in enumerate(dirs):
        if not dirNum == -1 and (i+2)%4 == dirNum:
            continue
        ny = y + dir[0]
        nx = x + dir[1]

        if not canGo(place,ny,nx):
            continue
        if place[ny][nx] == 'P':
            return False

        if not isGood(place,d-1,i,ny,nx):
            return False
    return True
    

def solution(places):
    answer = []
    
    for place in places:
        flag = True
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == 'P' and not isGood(place,2, -1, i,j):
                    answer.append(0)
                    flag = False
                    break

            if flag == False:
                break
        if flag == True:
            answer.append(1)
        #P 2칸 확인 dfs ->
        
    
    
    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))