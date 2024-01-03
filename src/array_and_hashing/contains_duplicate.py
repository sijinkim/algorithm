"""
2024-01-03

217.Contains Duplicate(https://leetcode.com/problems/contains-duplicate)
"""
from collections import Counter

from pydantic import BaseModel

from src import timer


class ContainsDuplicateSolution(BaseModel):
    nums: list[int]

    @timer
    def duplicate_check(self) -> bool:
        num_counter = Counter(self.nums)
        if num_counter.total() > len(num_counter):
            return True
        return False

    @timer
    def duplicate_check_faster(self) -> bool:
        count: dict[int, int] = {}
        for n in self.nums:
            try:
                count[n] += 1
            except KeyError:
                count[n] = 1
            else:
                return True
        return False

    @timer
    def duplicate_check_more_faster(self) -> bool:
        """
        #1. sort -> set의 bad case인 BigO(n) 보다 작은 sorting 알고리즘 적용 필요
        #2. sorting 과정에서 동일한 item 있으면 return True
        #3. sorting이 완료되면 return False

        sorting 알고리즘 Worst(BigO) 확인 결과, Heap Sort/Merge Sort O(n log(n))
        set(...) n이 큰 worst case에서 O(n)보다 결과 나쁨

        때문에 #1,2,3 대신 set.add (O(1)) 를 활용한다.
            1. n = 0 짜리 set 생성
            2. nums iter 돌면서 set에 element가 있는지 확인
            3. 없으면 set.add / 있으면 return True 종료
        """
        check_set: set[int] = set()
        for n in self.nums:
            if n in check_set:
                return True
            check_set.add(n)
        return False

    def __repr__(self) -> str:
        return f"ContainsDuplicateSolution object: {id(self)}"
