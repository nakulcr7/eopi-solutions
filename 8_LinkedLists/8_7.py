from node import *


def remove_kth_last(list_node, k):
    dummy_head = Node(0, list_node)
    fast = dummy_head.next
    while k > 0:
        fast = fast.next
        k -= 1
    second = dummy_head
    while fast is not None:
        second = second.next
        fast = fast.next

    second.next = second.next.next
    return dummy_head.next


def main():
    assert get_list_from_head(remove_kth_last(get_test_list_1(), 2)) == [1, 5]
    assert get_list_from_head(remove_kth_last(get_test_list_1(), 1)) == [1, 3]
    assert get_list_from_head(remove_kth_last(get_test_list_1(), 3)) == [3, 5]


if __name__ == '__main__':
    main()
