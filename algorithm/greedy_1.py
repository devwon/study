# greedy algorithm 이용한 거스름돈 문제
import sys
input = sys.stdin.readline
amount = int(input())


def get_count_of_changes(amount: int) -> int:
    # 화폐 단위 array
    coins = [500, 100, 50, 10]
    count = 0

    for coin in coins:
        count += amount // coin
        amount %= coin

    return count


res = get_count_of_changes(amount)
print('최소 거스름돈 개수', res)
