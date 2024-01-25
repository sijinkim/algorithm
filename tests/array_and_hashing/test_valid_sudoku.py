import pytest

from src.array_and_hashing import ValidSudokuSolution


@pytest.fixture
def boards() -> list[list[list[str]]]:
    return [
        [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ],
        [
            [".", ".", "4", ".", ".", ".", "6", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["5", ".", ".", ".", ".", ".", ".", "9", "."],
            [".", ".", ".", "5", "6", ".", ".", ".", "."],
            ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
            [".", ".", ".", "7", ".", ".", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
        ],
    ]


def test_is_valid_board(boards):
    assert ValidSudokuSolution(board=boards[0]).is_valid_sudoku() == True
    assert ValidSudokuSolution(board=boards[1]).is_valid_sudoku() == False


def test_is_valid_board_using_set(boards):
    assert ValidSudokuSolution(board=boards[0]).is_valid_sudoku_using_set() == True
    assert ValidSudokuSolution(board=boards[1]).is_valid_sudoku_using_set() == False
