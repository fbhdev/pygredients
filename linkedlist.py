from node import Node
from typing import Any
from abc import abstractmethod, ABC

class LinkedListInterface(ABC):
    """Defines the interface for the Linked List data structure."""

    @abstractmethod
    def __init__(self, limit=None) -> None:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def append(self, data: Any) -> None:
        pass

    @abstractmethod
    def remove(self, data: Any) -> Any:
        pass

    @abstractmethod
    def peek(self) -> Any:
        pass

    @abstractmethod
    def contain(self, data: Any) -> bool:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        pass


class LinkedList(LinkedListInterface):
    """Defines a Linked List data structure."""

    def __init__(self, limit=None) -> None:
        """
        Constructor for the Linked List data structure.
        :param limit:
        """
        if not limit: self.limit = float("inf")
        else: self.limit = limit
        self._size: int = 0
        self.head = None

    def __str__(self) -> str:
        """
        Returns a string representation of the Linked List data structure to display.
        :return: str
        """
        data = []
        current = self.head
        while current is not None:
            data.append(current.data)
            current = current.next
        return "LinkedList has a size of {}\n{}".format(self._size, data)

    def __repr__(self) -> str:
        """
        Returns a string representation of the Linked List data structure to debug.
        :return: str
        """
        return "LinkedList({})".format(self._size)

    def append(self, data: Any) -> None:
        """
        Appends the data to the Linked List data structure.
        :param data: Any
        :return: None
        """
        if self._size == self.limit:
            raise IndexError("Cannot append {} to Linked List as it is full.".format(data))
        self.head = Node(data, self.head)
        self._size += 1

    def remove(self, data: Any) -> Any:
        """
        Removes the data from the Linked List data structure.
        :param data: Any
        :return: Any
        """
        if self.is_empty():
            raise IndexError("Cannot remove {} from an empty Linked List.".format(data))
        current = self.head
        previous = None
        while current is not None:
            if data == current.data:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                self._size -= 1
                return current.data
            previous = current
            current = current.next
        raise IndexError("Cannot remove {} from Linked List as it does not exist.".format(data))

    def peek(self) -> Any:
        """
        Returns the first item in the Linked List data structure.
        :return: Any
        """
        if self.is_empty():
            raise IndexError("Cannot peek an empty Linked List.")
        return self.head.data

    def contain(self, data: Any) -> bool:
        """
        Returns whether the Linked List data structure contains the data.
        :param data: Any
        :return: bool
        """
        if self.is_empty(): raise IndexError("Linked List does not contain {} as it is empty.".format(self._size))
        current = self.head
        while current is not None:
            if data == current.data:
                return True
            current = current.next
        return False

    def size(self) -> int:
        """
        Returns the size of the Linked List data structure.
        :return: int
        """
        return self._size

    def is_empty(self) -> bool:
        """
        Returns whether the Linked List data structure is empty.
        :return: bool
        """
        return self._size == 0