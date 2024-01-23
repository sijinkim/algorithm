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

        - 다시 계산 -
        0.2143ms
        """
        counter: Counter[int] = Counter(self.nums)
        return [x[0] for x in counter.most_common(self.k)]

    @timer
    def top_k_frequent_with_bucket_sort(self) -> list[int]:
        """
        0. self.nums 길이만큼 array를 만들고
        1. self.nums N 만큼 돌면서 counter dict 생성 -> O(N)
        2. counting 개수를 array index로, element를 value로 array에 저장 -> O(N)
        3. array 뒤부터 순회하면서, Max element 뽑기 -> O(K)

        O(N)
        0.0321
        """
        counter: dict[int,int] = {}
        bucket: list[list[int]] = [[] for x in range(len(self.nums) + 1)]

        for n in self.nums: # O(N)
            counter[n] = 1 + counter.get(n, 0)
        
        for n,c in counter.items(): # O(N)
            bucket[c].append(n)
        
        result: list[int] = []
        count = len(self.nums)
        while len(result) < self.k: # O(K)
            if bucket[count]:
                result += bucket[count]
            count -= 1
        
        return result
            

        
