'''
https://school.programmers.co.kr/learn/courses/30/lessons/67259
3차원 배열로 방향을 아예 박는 걸로 하면 여러 방향을 고려할 수가 있음
'''
def check_range(x,y,H,W):
    if 0<=x<W and 0<=y<H:
        return True
    return False

def solution(board):
    X = [-1,0,0,1]
    Y = [0,1,-1,0]
    H = len(board)
    W = len(board[0])
    tmp = [[[0]*W for _ in range(H)] for _ in range(4)]
    print(tmp)
    # 서 : 0  남 : 1  북 : 2  동 : 3
    queue = []
    # 처음 갱신
    for i in range(4):
        dx = X[i]
        dy = Y[i]
        if check_range(dx,dy,H,W) and board[dy][dx] == 0:
            # [방향, 길이]
            tmp[i][dy][dx] = 100
            queue.append([dy,dx,i])
    while queue:
        y,x,direction = queue.pop()
        price = tmp[direction][y][x]
        for i in range(4):
            dx = x + X[i]
            dy = y + Y[i]
            if dx == 0 and dy == 0 : continue
            if check_range(dx,dy,H,W) and board[dy][dx] == 0:
                # 이미 값이 있었다면 비교
                if tmp[i][dy][dx] != 0:
                    len_ = tmp[i][dy][dx]
                    # 방향 같다면
                    tmp_len = 0
                    if i == direction:
                        tmp_len = 100
                    else:
                        tmp_len = 600
                    if len_ > tmp_len + price:
                        tmp[i][dy][dx] = tmp_len+ price
                        queue.append([dy,dx,i])
                else:
                    #값이 없었다면
                    if i == direction:
                        tmp_len = price + 100
                    else:
                        tmp_len = price + 600
                    tmp[i][dy][dx] = tmp_len
                    queue.append([dy,dx,i])
    min_ = 10**10
    for i in range(4):
        if tmp[i][H-1][W-1] == 0: continue
        print(tmp[i][H-1][W-1])
        min_ = min(min_,tmp[i][H-1][W-1])
    for i in range(4):
        for j in range(H):
            print(*tmp[i][j])
        print()
    return min_
           

# 직선도로 100원
# 코너 500원 -> 그 전방향이 뭔지 파악해야 함
# 동 : 0  남: 1  서 : 2  북 : 3
        
                    
print(solution([[0,1,0],[0,0,0],[1,0,0]]))
                        
                    
            
            
