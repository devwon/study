# [구현] 왕실의 나이트 문제
def royal_knight(input_data: str) -> int:
    row = int(input_data[1])    # 행
    col = int(ord(input_data[0]) - 96)

    # 이동할 수 있는 8가지 방향
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1),
             (2, 1), (1, 2), (-1, 2), (-2, 1)]

    # 이동가능한 방향 파악
    result = 0
    for step in steps:
        # 이동하고자 하는 위치 확인
        next_row = row + step[0]
        next_col = col + step[1]
        # 해당 위치로 이동이 가능할 시 count+1
        if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8:
            result += 1

    return result


# 현재 위치 입력 받기
input_data = input()
res = royal_knight(input_data)
print(res)

# (x+2, y+1)
# (x+2, y-1)
# (x-2, y+1)
# (x-2, y-1)
# (x+1, y+2)
# (x+1, y-2)
# (x-1, y+2)
# (x-1, y-2)

