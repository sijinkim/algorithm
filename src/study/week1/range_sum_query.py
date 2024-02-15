"""
2024-02-15

구간 합 구하기 4(https://www.acmicpc.net/problem/11659)
"""
import sys


def range_sum_query_solution() -> None:
    """
    1. nums 입력 순회하면서 prefix sum list 만들기 -> O(N)
    2. query 순회하면서 prefix sum list에서 누적합 계산하기 -> O(M)

    O(N) + O(M)
    """
    _input = sys.stdin.readline

    n, m = map(int, _input().split())
    nums: list[int] = list(map(int, _input().split()))
    assert len(nums) == n

    prefix_sum: list[int] = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)

    for _ in range(m):
        start, end = map(int, _input().split())
        print(prefix_sum[end] - prefix_sum[start - 1])
