def solution(clothes):
    answer = 1
    closet = []
    clothe_count = [0] * 30
    total_type = 0
    for clothe in clothes:
        if clothe[1] in closet:
            idx = closet.index(clothe[1])
            clothe_count[idx] += 1
        else:
            closet.append(clothe[1])
            total_type += 1
            idx = closet.index(clothe[1])
            clothe_count[idx] += 1

    for i in range(total_type):
        answer *= (clothe_count[i] + 1)

    return answer - 1