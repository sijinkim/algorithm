"""
2024-02-20

행렬과 연산 (https://school.programmers.co.kr/learn/courses/30/lessons/118670)
"""
from collections import deque


def shift_and_rotate_solution(
    rc: list[list[int]], operations: list[str]
) -> list[list[int]]:
    start: deque[int] = deque([])
    middle: deque[deque[int]] = deque([])
    end: deque[int] = deque([])

    for r in rc:  # queue 생성 O(r)
        start.append(r[0])
        middle.append(deque(r[1:-1]))
        end.append(r[-1])

    for ops in operations:  # O(operation length)
        if ops == "ShiftRow":
            start.appendleft(start.pop())  # O(1)
            middle.appendleft(middle.pop())  # O(1)
            end.appendleft(end.pop())  # O(1)
        else:
            middle[0].appendleft(start.popleft())
            end.appendleft(middle[0].pop())
            middle[-1].append(end.pop())
            start.append(middle[-1].popleft())

    # make answer form
    num_r = len(start)
    for idx in range(num_r):  # O(r)
        middle[idx].appendleft(start.popleft())  # O(1)
        middle[idx].append(end.popleft())  # O(1)

    return [list(m) for m in middle]
