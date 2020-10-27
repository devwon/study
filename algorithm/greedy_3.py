# greedy algorithm 이용한 곱하기 혹은 더하기 문제


def multiply_or_plus(data: str) -> int:
    # 첫 번째 문자를 숫자로 변경하여 대입
    result = int(data[0])

    for i in range(1, len(data)):
        # 두 수 중에서 하나라도 0 또는 1 인 경우, 더하기 수행
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num
    return result


data = input()
res = multiply_or_plus(data)
print(res)
