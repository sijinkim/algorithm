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
        1.1 장애물에 해당되는 idx에 +1
            1.1.1 장애물에 해당되는 idx 하나씩 돌면서 +1 => 최악 O(M)
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


def firefly_time_solution() -> None:
    """
    0. N: MAX 200_000, H: MAX 200_000 => N * H array 생성하여 처리? 공간 복잡도 터짐(N*M)
    1. 길이 H 짜리 석순 array, 종유석 array 생성
    2. N 만큼 순회하면서, => O(N)
        석순[해당 크기] += 1
        종유석[해당 크기] += 1
        * 길이가 몇짜리 석순/종유석이 동굴에 몇개가 있는지 카운트하기 위함
    3. 석순/종유석 뒤에서부터 누적합  => O(H)
        * 뒤에서부터 누적합하는 이유
        * 석순/종유석의 위치가 어떻게 되었든, 본인보다 높이가 낮은 길을 지나갈 때는 해당 석순/종유석을 뚫고 가야만 함
    4. H 만큼 순회하면서, => O(H)
        해당 높이로 지나갈 때, 석순/종유석 각각 몇개나 뚫어야하는지 체크(min value, min count)

    O(N) + O(H) + O(H)
    """
    _input = sys.stdin.readline

    n, h = map(int, _input().split())
    bottom: list[int] = [0] * (h + 1)  # 석순
    top: list[int] = [0] * (h + 1)  # 종유석

    for idx in range(n):  # O(N)
        height: int = int(_input())
        if idx % 2 == 0:  # 석순
            bottom[height] += 1
        else:  # 종유석
            top[height] += 1

    for idx in range(h - 1, 0, -1):  # O(H)
        bottom[idx] += bottom[idx + 1]
        top[idx] += top[idx + 1]

    min_value = n
    count = 0

    for idx in range(1, h+1):
        walls = bottom[idx] + top[h - idx + 1]
        if min_value == walls:
            count += 1

        elif min(min_value, walls) == walls:
            min_value = walls
            count = 1

    print(f"{min_value} {count}")
