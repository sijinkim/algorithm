"""
2024-01-25

36. Valid Sudoku (https://leetcode.com/problems/valid-sudoku/)
"""
from pydantic import BaseModel, validator

class ValidSudokuSolution(BaseModel):
    board: list[list[str]]

    @validator
    def board_check():
        ...

    def is_valid_sudoku(self) -> bool:
        """
        0. row check, column check, 3x3 sub-boxes check
        """