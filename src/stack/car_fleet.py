"""
2024-02-18

853. Car Fleet (https://leetcode.com/problems/car-fleet/)
"""
from pydantic import BaseModel


class CarFleetSolution:
    target: int
    position: list[int]
    speed: list[int]

    def solution(self) -> int:
        """
        1 <= n <= 100_000
        0 < target <= 1000_000

        n x target 으로 런타임 통과 불가함. 이중루프 돌지않고 car fleet 여부 확인하는 방법
        """
        ...
