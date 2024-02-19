"""
2024-02-18

853. Car Fleet (https://leetcode.com/problems/car-fleet/)
"""
from math import trunc

from pydantic import BaseModel


class CarFleetSolution(BaseModel):
    target: int
    position: list[int]
    speed: list[int]

    def solution(self) -> int:
        """
        고정된 정보를 활용하여 차들 간에 만날 수 밖에 없는지 확인
        0. 고정된 정보: 차들의 초기 위치 (self.position)
            A차의 초기 위치가 B차의 초기 위치보다 target으로부터 멀리 있는데,
            B차는 target까지 10초 걸리고
            A차는 target까지 5초 걸린다면
            A차와 B차는 만날 수밖에 없음.
            + A차는 B차에 dependency 생김
            + A차의 정보는 무의미함. B차의 정보만 활용

        1. 초기 위치가(position) target으로부터 가까운 순서대로 순회하면서 => O(N)
        2. target까지 도달하는 데 걸리는 시간(t) 체크하여 stack.put(t)
            2.1 만약 curr car t 값이 prev car t 값보다 작다면
                2.1.1 trunc(curr car t) == trunc(prev car t) -> 직접 만나지 않고 target에 각자 도달
                    pass
                2.1.2 trunc(curr car t) != trunc(prev car t) -> prev car와 target 전에 만남
                    curr car t pop
            2.2 만약 prev car t 값이, curr car t값과 동일하다면 (prev car 와 target에서 만남)
                curr car t pop
            2.3 크다면, pass
        """
        pairs: list[list[int]] = []
        stack: list[float] = []

        num_of_cars: int = len(self.position)

        for i in range(num_of_cars):  # O(N)
            pairs.append([self.position[i], self.speed[i]])

        pairs = sorted(pairs, reverse=True)

        for car_info in pairs:
            time = (self.target - car_info[0]) / car_info[1]

            stack.append(time)

            if len(stack) > 1:
                if stack[-2] > stack[-1]:  # car fleet 생성 케이스
                    if not trunc(stack[-2]) == trunc(stack[-1]):
                        # group car fleet
                        stack.pop()

                if stack[-2] == stack[-1]:
                    # group car fleet
                    stack.pop()

        return len(stack)
