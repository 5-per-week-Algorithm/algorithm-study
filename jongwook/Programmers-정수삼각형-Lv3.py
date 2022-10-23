def solution(triangle):
    answer = 0
    total_height = len(triangle) - 1

    while True:
        current_row = triangle[total_height]
        upper_row = triangle[total_height - 1]

        for i in range(len(upper_row)):
            if current_row[i] > current_row[i + 1]:
                upper_row[i] += current_row[i]
            else:
                upper_row[i] += current_row[i + 1]

        total_height -= 1

        if total_height <= 0:
            break

    return triangle[0][0]