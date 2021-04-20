#!/usr/bin/env python3
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, val: int = 0, next: Node=None):
        self.val = val
        self.next = next


"""7.1 Merge two sorted lists.

Write a program that takes two lists assumed to be sorted, and returns their
merge. The only field your program can change in a node is its next field.
"""

def merge_lists(l1: Node, l2: Node) -> Node:
    dummy_head = curr = Node()

    while l1 and l2:
        if l1.val < l2.val:
            curr.next, l1 = l1, l1.next
        else:
            curr.next, l2 = l2, l2.next
        curr = curr.next
    
    curr.next = l1 or l2
    return dummy_head.next

"""7.2 Reverse a single sublist.

Write a program which takes a singly linked list L and two integers s and f as
arguments, and reverses the order of the nodes from the sth node to the fth node,
inclusive. The numbering begins at 1. Do no allocate additional nodes.
"""

def reverse_sublist(l: Node, s: int, f: int) -> Node:
    dummy_head = sublist_head = Node(next=l)
    for _ in range(s - 1):
        sublist_head = sublist_head.next
    
    curr = sublist_head.next
    
    for _ in range(f - s):
        next = curr.next
        curr.next, next.next, sublist_head.next = next.next, sublist_head.next, next

    return dummy_head.next



"""7.3 Test for cyclicity.

Write a program that takes the head of a singly linked list and returns null if
there does not exist a cycle, and the node at the start of the cycle, if a cycle
is present. (You do not know the length of the list in advance).
"""

# see https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle
# for more.
def get_head_of_cycle(l: Node) -> Optional[Node]:
    slow = fast = l
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = l
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return None