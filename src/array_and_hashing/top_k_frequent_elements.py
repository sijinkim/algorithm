"""
2024-01-23

347. Top K Frequent Elements (https://leetcode.com/problems/top-k-frequent-elements/description/)
"""
from collections import Counter

from pydantic import BaseModel
from src.utils import timer

class TopKFrequentElementsSolution(BaseModel):
    nums: list[int]
    k: int

    @timer
    def top_k_frequent(self) -> list[int]:
        """
        0. Counter를 활용한 베이스 방법
        1. 주어진 int array nums 순회하면서 Counter dictionary 생성 -> 각 elements가 몇개씩 존재하는지 체크: O(N)
        2. most_common function -> value 사이즈 비교:  O(k) + O((n - k) log k) + O(k log k)

        0.2143ms
        """
        counter: Counter[int] = Counter(self.nums)
        return [x[0] for x in counter.most_common(self.k)]
