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
    def product_except_self_memory_exceeded(self) -> list[int]:
        """
        1. nums 순회하면서 hash 생성 {index: [except self elements]} => O(N)
        2. hash map 순회하면서 values 곱, 그 결과값을 result array로 => O(N) * O(N-1)

        #Memory Limit Exceeded
        O(N*N)
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

    @timer
    def product_except_self(self) -> list[int]:
        """
        0. 자기자신만 빼고, 앞 뒤로 다 곱한 값 필요. 앞!뒤! => index보다 작은 위치의 value 곱 * index보다 큰 위치의 value 곱
        1. self.nums 와 동일한 길이의 array A 생성
        2. 앞에서부터 A array 순회하면서 A array의 각 index에,
            self.nums에서 해당 index 보다 작은 elements 전체 곱한 값을 담음 => O(n)
        3. 뒤에서부터 A array 순회하면서 A array의 각 index에,
            self.nums에서 해당 index 보다 큰 elements 전체 곱한 값을 기존의 값(index보다 작은 위치의 값들 곱)과 곱 => O(n)
        4. A array return

        O(N)
        """
        idx_counter: int = len(self.nums)
        result: list[int] = [1] * idx_counter
        prefix_product: int = 1
        postfix_product: int = 1

        for i in range(idx_counter):  # O(N)
            result[i] = prefix_product
            prefix_product *= self.nums[i]
            # result array - 각 index 보다 작은 위치의 elements 들을 곱한 값이 각 index에 저장
            # result: (index보다 작은 위치의 elemts 곱)
        for i in range(idx_counter - 1, -1, -1):  # O(N)
            result[i] *= postfix_product
            postfix_product *= self.nums[i]

        return result
