"""
2024-01-29

Bot saves princess (https://www.hackerrank.com/challenges/saveprincess/problem)
"""

#!/usr/bin/python


def display_path_to_princess(grid: list[list[str]]) -> list[str]:
    # find princess
    princess = []
    bot = []
    for idx, line in enumerate(grid):
        if "p" in line:
            princess = [idx, line.index("p")]
        if "m" in line:
            bot = [idx, line.index("m")]

    result = []
    while bot != princess:
        if bot[0] > princess[0]:
            result.append("UP")
            bot[0] -= 1
        if bot[0] < princess[0]:
            result.append("DOWN")
            bot[0] += 1
        if bot[1] > princess[1]:
            result.append("LEFT")
            bot[1] -= 1
        if bot[1] < princess[1]:
            result.append("RIGHT")
            bot[1] += 1

    return result
