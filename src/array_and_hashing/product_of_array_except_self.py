"""
2024-01-24

238. Product of Array Except Self 
(https://leetcode.com/problems/product-of-array-except-self/description/)
"""
from pydantic import BaseModel

from src.utils import timer


class ProductOfArrayExceptSelfSolution(BaseModel):
    nums: list[int]

    @timer
    def product_except_self(self) -> list[int]:
        """
        1. nums 순회하면서 hash 생성 {index: [except self elements]} => O(N)
        2. hash map 순회하면서 values 곱, 그 결과값을 result array로 => O(N) * O(N-1)

        #Memory Limit Exceeded
        """
        except_self_dict: dict[int, list[int]] = {}

        for idx in range(len(self.nums)):
            copy_nums: list[int] = self.nums.copy()
            copy_nums.pop(idx)
            except_self_dict[idx] = copy_nums

        result: list[int] = [1] * len(self.nums)
        for idx, values in except_self_dict.items():
            for element in values:
                result[idx] *= element

        return result
