"""
2024-02-20

캐시 (https://school.programmers.co.kr/learn/courses/30/lessons/17680)
"""
from collections import deque


def cache_solution(cache_size: int, cities: list[str]) -> int:
    answer: int = 0
    cache: deque[str] = deque([])

    for city in cities:
        city = city.lower()

        if city in cache:  # 캐시에 해당 나라 정보가 있는 경우
            answer += 1
            cache.remove(city)

        else:  # 캐시에 없는 경우
            answer += 5

        # 캐시 LRU
        if cache_size != 0:
            if len(cache) == cache_size:
                cache.popleft()

            cache.append(city)

    return answer
