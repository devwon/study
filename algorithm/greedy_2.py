# greedy algorithm 이용한 1이 될 때까지 문제


def til_become_one(n: int, k: int) -> int:
    result = 0

    while True:
        # n이 k로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
        target = (n // k) * k
        result += (n - target)
        n = target
        # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) break
        if n < k:
            break
        result += 1
        # k로 나누기
        n //= k

    # 마지막으로 남은 수에 대하여 1씩 빼기
    result += (n - 1)

    return result


# n, k를 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

res = til_become_one(n, k)

print(res)
