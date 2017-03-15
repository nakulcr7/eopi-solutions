from node import *


def find_cycle(head):
    fast = slow = head
    while fast is not None and fast.next is not None and fast.next.next is not None:
        fast = fast.next
        slow = slow.next
        if slow == fast:  # There is a cycle
            slow = head
            # Both pointers advance at the same time
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None
