import numpy as np
import pandas as pd
from pandas.testing import assert_frame_equal

from src.ml import login_table


def test_can_merge():
    id_name_verified = pd.DataFrame(
        [[1, "JohnDoe", True], [2, "AnnFranklin", False]],
        columns=["Id", "Login", "Verified"],
    )
    id_password = np.array([[1, 100], [2, 200]], np.int32)

    login_table(id_name_verified, id_password)
    assert_frame_equal(
        id_name_verified,
        pd.DataFrame(
            [[1, "JohnDoe", 100], [2, "AnnFranklin", 200]],
            columns=["Id", "Login", "Password"],
        ),
        check_dtype=False,
    )


def test_can_merge_by_Id_key():
    id_name_verified = pd.DataFrame(
        [[2, "JohnDoe", True], [1, "AnnFranklin", False], [1, "AnnFranklin", False]],
        columns=["Id", "Login", "Verified"],
    )
    id_password = np.array([[1, 100], [2, 200]], np.int32)

    login_table(id_name_verified, id_password)
    assert_frame_equal(
        id_name_verified,
        pd.DataFrame(
            [[2, "JohnDoe", 200], [1, "AnnFranklin", 100], [1, "AnnFranklin", 100]],
            columns=["Id", "Login", "Password"],
        ),
        check_dtype=False,
    )
