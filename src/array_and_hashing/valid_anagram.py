"""
2023-01-06

242.Valid Anagram (https://leetcode.com/problems/valid-anagram)
"""
from pydantic import BaseModel

class ValidAnagramSolution(BaseModel):
    s: str
    t: str

    def isAnagram(self) -> bool:
        ...