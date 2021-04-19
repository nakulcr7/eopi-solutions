#!/usr/bin/env python3
from collections import deque, namedtuple
from typing import List


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


"""8.6 Compute binary tree notes in order of increasing depth.

Given a binay tree, return an array consisting of keys at the same level. Keys
should appear in the order of the corresponding nodes' depths, breaking ties
from left to right.
"""

class Node:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
    

# Note: you don't need queues to solve this problem. See binary_trees.py for a
# more concise solution.

def binary_tree_depth_order(tree: Node) -> List[List[int]]:
    curr_level_nodes = deque(tree)
    res = []

    while curr_level_nodes:
        next_level_nodes, curr_level_values = deque(), [] 
        while curr_level_nodes:
            curr = curr_level_nodes.popleft()
            if curr:
                curr_level_values.append(curr.val)
                next_level_nodes += [curr.left, curr.right]
        if curr_level_values:
            res.append(curr_level_values)
        curr_level_values = next_level_nodes

    return ret


