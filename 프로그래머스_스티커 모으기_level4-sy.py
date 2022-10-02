'''
1. backtracking으로 for문을 돌면서 차례로 스티커를 뜯어내기
    - 재귀로 뜯어낸 다음 다시 붙이기
'''
stickers = [1, 3, 2, 5, 4]
max_ = -1

def collect(stickers,answer):
    global max_
    if stickers == []:
        max_ = max(max_,answer)
        return
    for idx, sticker in enumerate(stickers):
        new_answer = answer + stickers[idx]
        tmp = []
        if idx == 0:
            for j in range(len(stickers)):
                if j == (idx+1)%len(stickers) or j == (idx)%len(stickers):
                    continue
                tmp.append(stickers[j])
        elif idx == len(stickers)-1:
            for j in range(len(stickers)):
                if j == (idx-1)%len(stickers) or j == (idx)%len(stickers):
                    continue
                tmp.append(stickers[j])
        else:
            for j in range(len(stickers)):
                if j == (idx+1)%len(stickers) or j == (idx-1)%len(stickers) or j == (idx)%len(stickers):
                    continue
                tmp.append(stickers[j])
        collect(tmp,new_answer)

#떼어내는 부분
for idx in range(len(stickers)):
    tmp = []
    end = (idx - 2) % len(stickers)
    start = (idx + 2) % len(stickers)
    if start > end:
        end += len(stickers)
    for j in range(start,(end+1)):
        tmp.append(stickers[j%len(stickers)])
    collect(tmp,stickers[idx])

print(max_)
