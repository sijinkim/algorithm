"""
2024-01-25

36. Valid Sudoku (https://leetcode.com/problems/valid-sudoku/)
"""
from pydantic import BaseModel, field_validator

from src.utils import timer


class ValidSudokuSolution(BaseModel):
    board: list[list[str]]

    @field_validator("board")
    @classmethod
    def board_check(cls, values: list[list[str]]) -> list[list[str]]:
        if not len(values) == 9:
            raise ValueError("must 9 rows")

        for column in values:
            if not len(column) == 9:
                raise ValueError("must 9 columns")

            for element in column:
                if not isinstance(element, str):
                    raise ValueError("must string type")
        return values

    @timer
    def is_valid_sudoku(self) -> bool:
        """
        0. row check, column check, 3x3 sub-boxes check:
            row 확인용 hash, column 확인용 hash array, 3x3 sub boxes 확인용 hash array 생성
        1. self.board[i] 순회하면서, => O(N) * O(N)
            1-1. row hash[i][j], if int in row hash key: not valid board
            1-2. column hash array[j], if int in column hash array[j] key: not valid board
            1-3. 3x3 sub boxes hash array[i//3*3 + j//3],
                if int in sub boxes hash array[i//3*3 + j//3] key: not valid board

        O(1) : N이 9로 fix되어 있으므로
        0.0600ms
        """
        row_checker: dict[str, bool]
        column_checker: list[dict[str, bool]] = [{} for _ in range(9)]
        sub_checker: list[dict[str, bool]] = [{} for _ in range(9)]

        for i in range(9):  # O(N^2)
            row_checker = {}
            for j in range(9):
                num: str = self.board[i][j]
                if num == ".":
                    continue  # next j

                if num in row_checker:  # row check
                    return False

                if num in column_checker[j]:  # column check
                    return False

                if num in sub_checker[i // 3 * 3 + j // 3]:  # sub boxes check
                    return False

                row_checker[num] = True
                column_checker[j][num] = True
                sub_checker[i // 3 * 3 + j // 3][num] = True

        return True

    @timer
    def is_valid_sudoku_using_set(self) -> bool:
        """
        0. board 길이가 고정되어 있는 점 활용. board 다 훑어보고,
            row / column / sub box 별로 "index, value" 가 unique한지 확인

        0.0440ms
        """
        result: list[tuple[int, str] | tuple[str, int] | tuple[int, int, str]] = []

        for i in range(9):
            for j in range(9):
                num = self.board[i][j]
                if not num == ".":
                    result += [
                        (i, num),
                        (num, j),
                        (i // 3, j // 3, num),
                    ]  # row check, column check, sub-box check

        return len(result) == len(set(result))
