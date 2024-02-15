"""
2024-02-14

739.Daily Temperatures (https://leetcode.com/problems/daily-temperatures/)
"""
from src.utils import timer


class DailyTemperaturesSolution:
    @timer
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        """
        basic solution

        temperatures 하나씩 순회하면서 더 큰 값 나올 때까지 count up

        O(N*N)
        0.0181ms
        """
        days = len(temperatures)
        result = [0] * days
        for t in range(0, days):
            for i in range(t + 1, days):
                if temperatures[t] >= temperatures[i]:
                    result[t] += 1

                if temperatures[t] < temperatures[i]:
                    result[t] += 1
                    break

                if i == days - 1 and temperatures[t] >= temperatures[i]:
                    result[t] = 0

        return result

    @timer
    def daily_temperatures_stack_hashmap(self, temperatures: list[int]) -> list[int]:
        """
        1. temperatures 순회하면서 => O(N)
            {each_temp: (greater_value, idx)} -> greater value가 나왔을 때,hashmap에 추가되도록
        2. hashmap 참고하여 result list 생성 - 날짜 카운트, no warmer day 처리

        O(N) + O(N)
        0.0260ms
        """
        greater_hash: dict[str, tuple[int, int]] = {}
        waiting_stack: list[tuple[int, int]] = []
        result: list[int] = []

        for idx, num in enumerate(temperatures):
            while waiting_stack and num > waiting_stack[-1][0]:
                greater_hash[str(waiting_stack.pop())] = (
                    num,
                    idx,
                )  # curr_temp: (greater_value, idx)

            waiting_stack.append((num, idx))

        for idx, num in enumerate(temperatures):
            if str((num, idx)) in greater_hash:
                result.append(greater_hash.pop(str((num, idx)))[1] - idx)

            else:
                result.append(0)

        return result

    @timer
    def daily_temperatures_stack(self, temperatures: list[int]) -> list[int]:
        """
        1. temperatures 순회하면서 => O(N)
            hashmap 만들지말고, result list 바로 생성 - 날짜 카운트, no warmer day 처리

        O(N)
        0.0175ms
        """
        waiting_stack: list[tuple[int, int]] = []
        result: list[int] = [0] * len(temperatures)

        for idx, num in enumerate(temperatures):
            while waiting_stack and num > waiting_stack[-1][0]:
                result[waiting_stack.pop()[1]] = idx - waiting_stack[-1][1]

            waiting_stack.append((num, idx))

        return result
