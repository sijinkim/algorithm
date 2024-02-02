"""
2024-02-02

Login Table 
(https://www.testdome.com/library?page=1&skillArea=97&questionSets=public&questionId=81252)
"""
from typing import Any

import numpy.typing as npt
import pandas as pd


def login_table(id_name_verified: pd.DataFrame, id_password: npt.NDArray[Any]) -> None:
    """
    :param id_name_verified: (DataFrame) DataFrame with columns: Id, Login, Verified.
    :param id_password: (numpy.array) Two-dimensional NumPy array where each element
                        is an array that contains: Id and Password
    :returns: (None) The function should modify id_name_verified DataFrame in-place.
              It should not return anything.
    """
    id_name_verified.drop(["Verified"], axis=1, inplace=True)

    for row in id_password:
        user_id, password = row
        # Locate the row with the corresponding user_id in id_name_verified DataFrame
        index = id_name_verified.index[id_name_verified["Id"] == user_id].tolist()

        # Check if the user_id exists in id_name_verified DataFrame
        for idx in index:
            # Update the Password column in-place
            id_name_verified.at[idx, "Password"] = int(password)
