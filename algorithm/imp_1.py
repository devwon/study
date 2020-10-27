# [구현] 시각 완전 탐색 문제 유형


def is_contain_sth(h: int) -> int:
    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
                if '3' in str(i) + str(j) + str(k):
                    count += 1
    return count


# H 입력 받기
h = int(input())
res = is_contain_sth(h)
print(res)

