def leftToRank(left):
    if left > 4:
        return 6
    return left+1
    


def solution(lottos, win_nums):
    bonus = lottos.count(0)
    
    for num in lottos:
        if num in win_nums:
            win_nums.remove(num)
    left = len(win_nums)
    return [leftToRank(left - bonus), leftToRank(left)]