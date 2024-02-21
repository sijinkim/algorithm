"""
2024-02-21

기능개발 (https://school.programmers.co.kr/learn/courses/30/lessons/42586)
"""
import math


def develop_function_solution(progresses: list[int], speeds: list[int]) -> list[int]:
    """
    progresses 의 작업 순서는 고정되어 있다.
    해당 순서대로 배포 가능하며, 당일까지 작업완료된 것들 묶어서 한번에 배포된다.
    즉, 뒤에 이어진 작업들이 popleft 작업 완료 전까지 완료되는지 확인 필요

    1. progresses 순회하면서 => O(N)
    2. 작업 완료까지 걸리는 시간 t 계산
        2.1 t가 앞선 작업보다 작업 시간이 덜 걸리면 함께 배포
        2.2 t가 앞선 작업보다 작업 시간이 더 걸리면 따로 배포
    """
    result: list[int] = []
    num_func: int = len(progresses)

    job_group: list[int] = []
    for i in range(num_func):
        time = math.ceil((100 - progresses[i]) / speeds[i])

        if len(job_group) >= 1:
            if job_group[0] >= time:
                pass  # 함께 배포
            else:  # 따로 배포
                result.append(len(job_group))
                job_group = []

        job_group.append(time)

    if job_group:
        result.append(len(job_group))  # 마지막 작업 처리

    return result
