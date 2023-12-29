"""
2023-12-29

Design Singly Linked List https://neetcode.io/problems/singlyLinkedList
"""
from dataclasses import dataclass


@dataclass
class Node:
    dist_from_head: int
    value: int
    dist_from_tail: int


class LinkedList:
    def __init__(self) -> None:
        self._nodes: list[Node] = []
        self._number_of_nodes: int = 0

    def get(self, index: int) -> int:
        if index < 0:
            raise ValueError("Index must be greater than or equal to 0.")

        if index >= self._number_of_nodes:
            return -1

        for n in self._nodes:
            if n.dist_from_head == index:
                return n.value
        return -1

    def insert_head(self, val: int) -> None:
        for n in self._nodes:
            n.dist_from_head += 1

        new_head = Node(
            dist_from_head=0, value=val, dist_from_tail=self._number_of_nodes
        )

        self._nodes.append(new_head)
        self._number_of_nodes += 1

    def insert_trail(self, val: int) -> None:
        for n in self._nodes:
            n.dist_from_tail += 1

        new_tail = Node(
            dist_from_head=self._number_of_nodes, value=val, dist_from_tail=0
        )

        self._nodes.append(new_tail)
        self._number_of_nodes += 1

    def remove(self, index: int) -> bool:
        if index < 0:
            raise ValueError("Index must be greater than or equal to 0.")

        if index >= self._number_of_nodes:
            return False

        curr_nodes = self._nodes.copy()
        for n in curr_nodes:
            if n.dist_from_head < index:
                n.dist_from_tail -= 1

            elif n.dist_from_head > index:
                n.dist_from_head -= 1

            else:
                self._nodes.remove(n)
                self._number_of_nodes -= 1

        return True

    def get_values(self) -> list[int]:
        values: list[int] = [0 for i in range(self._number_of_nodes)]

        for n in self._nodes:
            values[n.dist_from_head] = n.value

        return values
