def solution(n):
    answer = 0
    land = [0 for _ in range(2001)]
    land[0] = 1
    land[1] = 1
    for i in range(2,n+1):
        land[i] = (land[i] + land[i-1]) % 1234567
        land[i] = (land[i-2] + land[i]) % 1234567
    answer = land[n]
    return answer