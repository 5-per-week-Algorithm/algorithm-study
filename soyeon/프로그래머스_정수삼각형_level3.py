def solution(triangle):
    list_ = [[0]*len(triangle) for _ in range(len(triangle[-1]))]
    list_[0][0] = triangle[0][0]
    for i in range(1,len(triangle)):
        list_[i][0] = list_[i-1][0] + triangle[i][0]
        list_[i][len(triangle[i])-1] = list_[i-1][len(triangle[i])-2] + triangle[i][len(triangle[i])-1]
        for j in range(1,len(triangle[i])-1):
            list_[i][j] = max(list_[i-1][j],list_[i-1][j-1])+triangle[i][j]
    return max(list_[-1])