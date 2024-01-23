"""
2024-01-24

238. Product of Array Except Self (https://leetcode.com/problems/product-of-array-except-self/description/)
"""
from pydantic import BaseModel

class ProductOfArrayExceptSelfSolution(BaseModel):
    nums: list[int]

    def productExceptSelf(self) -> list[int]:
        ...