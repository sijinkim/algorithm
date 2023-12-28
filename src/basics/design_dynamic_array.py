"""
2023-12-28

Design Dynamic Array (Resizable Array) https://neetcode.io/problems/dynamicArray
"""


def check_array_empty(arr: list[int]) -> bool:
    return len(arr) == 0


class DynamicArray:
    def __init__(self, capacity: int):
        self._array: list[int] = []

        if not capacity > 0:
            raise ValueError("Array capacity must be greater than 0.")
        self._capacity: int = capacity

    def get(self, i: int) -> int:
        if check_array_empty(self._array):
            raise IndexError("The array is empty.")

        if i >= len(self._array):
            raise IndexError(
                "The index is greater than the number of elements in the array."
            )

        if i < 0:
            raise IndexError("The index is less than 0.")

        return self._array[i]

    def set_new_value(self, i: int, n: int) -> None:
        if i >= len(self._array):
            raise IndexError(
                "The index is greater than the number of elements in the array."
            )

        if i < 0:
            raise IndexError("The index is less than 0.")

        self._array[i] = n

    def pushback(self, n: int) -> None:
        if len(self._array) == self._capacity:
            self.resize()

        self._array.append(n)

    def popback(self) -> int:
        if check_array_empty(self._array):
            raise IndexError("The array is empty.")

        return self._array[-1]

    def resize(self) -> None:
        self._capacity = 2 * self._capacity

    def get_size(self) -> int:
        return len(self._array)

    def get_capacity(self) -> int:
        return self._capacity
