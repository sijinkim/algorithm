"""
2023-12-29

Design Singly Linked List https://neetcode.io/problems/singlyLinkedList
"""
from typing import Union


class ListNode:
    def __init__(self, value: int, next_node: Union["ListNode", None] = None):
        self._value = value
        self._next = next_node

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, val: int) -> None:
        self._value = val

    @property
    def next(self) -> Union["ListNode", None]:
        return self._next

    @next.setter
    def next(self, next_node: Union["ListNode", None]) -> None:
        self._next = next_node


class LinkedList:
    def __init__(self) -> None:
        self.head = ListNode(value=-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        if index < 0:
            raise ValueError("Index must be greater than or equal to 0.")

        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.value
            curr = curr.next
            i += 1
        # index 도달하기 전 None(tail.next) 만난 경우
        return -1

    def insert_head(self, val: int) -> None:
        new_node = ListNode(value=val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            # dummy node 제외, 최초 node일 경우
            self.tail = new_node

    def insert_trail(self, val: int) -> None:
        self.tail.next = ListNode(value=val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        if index < 0:
            raise ValueError("Index must be greater than or equal to 0.")

        curr: ListNode | None = self.head

        # curr을 index 직전 노드로 위치
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1

        # out of bounds index 방지를 위해 curr.next 유무도 점검
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def get_values(self) -> list[int]:
        curr = self.head.next
        results = []

        while curr:
            results.append(curr.value)
            curr = curr.next
        return results
