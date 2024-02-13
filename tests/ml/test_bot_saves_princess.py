import pytest

from src.ml import display_path_to_princess


@pytest.fixture
def inputs():
    grid = [["-", "-", "-"], ["-", "m", "-"], ["p", "-", "-"]]
    m = len(grid)
    return m, grid


def test_can_print_paths(inputs) -> str:
    assert display_path_to_princess(inputs[1]) == ["DOWN", "LEFT"]
