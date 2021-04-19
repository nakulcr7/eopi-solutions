#!/usr/bin/env python3
from typing import List
from collections import deque, namedtuple


class Stack:
    def __init__(self) -> None:
        self._s: List[int] = []
        self._size: int = 0
    
    @property
    def size(self) -> int:
        return self._size
    
    def push(self, x: int) -> None:
        self._s.append(x)
        self._size += 1
    
    def pop(self) -> int:
        if self.size < 1:
            raise IndexError("stack is empty.")
        return self._s.pop()
    
    def peek(self) -> int:
        if self.size < 1:
            raise IndexError("stack is empty.")
        return self._s[-1]


class Queue:
    def __init__(self) -> None:
        self._q = deque([])
        self._size: int = 0
    
    @property
    def size(self) -> int:
        return self._size
    
    def enqueue(self, x: int) -> None:
        self._q.append(x)
        self._size += 1
    
    def dequeue(self) -> int:
        if self.size < 1:
            raise IndexError("stack is empty.")
        return self._q.popleft()
    
    def peek(self) -> int:
        if self.size < 1:
            raise IndexError("stack is empty.")
        return self._q[-1]


"""8.1 Implement a stack with a max API.

Design a stack that includes a max operation, in addition to push and pop. The
max method should return the maximum value stored in the stack.
"""

class StackWithMax:
    ElemWithMax = namedtuple("ElemWithMax", ("elem", "max"))

    def __init__(self) -> None:
        self._s: List[self.ElemWithMax] = []
        self._size: int = 0
    
    @property
    def size(self) -> int:
        return self._size
    
    @property
    def is_empty(self) -> bool:
        return self._size == 0

    def push(self, x: int) -> None:
        max_so_far = self.peek().max if not self.is_empty else float("-inf")
        self._s.append(self.ElemWithMax(x, max(x, max_so_far)))
        self._size += 1
    
    def pop(self) -> int:
        if self.is_empty:
            raise IndexError("stack is empty.")
        return self._s.pop().elem
    
    def peek(self) -> int:
        if self.is_empty:
            raise IndexError("stack is empty.")
        return self._s[-1]
    
    @property
    def max(self) -> int:
        return self._s[-1].max