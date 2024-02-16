"""
2024-02-15

개똥벌레 (https://www.acmicpc.net/problem/3020)
"""
import sys
from collections import Counter


def firefly_solution() -> None:
    """
    0. N: MAX 200_000, M: MAX 200_000 => N * M array 생성하여 처리? 공간 복잡도 터짐(N*M)
    1. 길이 M array를 하나 생성하고, N 만큼 순회하면서 => O(N)
    2. 장애물에 해당되는 idx에 +1
        2.1 장애물에 해당되는 idx 하나씩 돌면서 +1 => 최악 O(M)
    3. M array에서 최소값 카운트해서 반환 => O(M)

    O(N * M) + O(M)

    시간 초과
    """
    _input = sys.stdin.readline

    n, m = map(int, _input().split())
    result: list[int] = [0] * (m + 1)

    for idx in range(n):
        wall = int(_input())
        for i in range(wall):
            if idx % 2 == 0:
                result[i + 1] += 1
            else:
                result[-(i + 1)] += 1

    count_result = Counter(result[1:])
    minimum = count_result.most_common()[-1][0]
    print(f"{minimum} {count_result[minimum]}")
