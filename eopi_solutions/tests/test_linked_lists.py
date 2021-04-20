#!/usr/bin/env python3

import unittest
from typing import List

from eopi_solutions import linked_lists as ll


def linked_list_to_list(l: ll.Node) -> List[int]:
    vals = []
    while l:
        vals.append(l.val)
        l = l.next
    return vals


class TestLinkedLists(unittest.TestCase):
    def test_merge_lists(self) -> None:
        l1 = ll.Node(2, ll.Node(5, ll.Node(7)))
        l2 = ll.Node(3, ll.Node(11))
        self.assertListEqual(linked_list_to_list(ll.merge_lists(l1, l2)), [2, 3, 5, 7, 11])
    
    def test_reverse_sublist(self) -> None:
        l = ll.Node(11, ll.Node(3, ll.Node(5, ll.Node(7, ll.Node(2)))))
        self.assertListEqual(linked_list_to_list(ll.reverse_sublist(l, 2, 4)), [11, 7, 5, 3, 2])