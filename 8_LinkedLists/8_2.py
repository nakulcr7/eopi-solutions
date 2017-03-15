from node import *


def reverse_sublist(list_node, start, end):
    if start == end:
        return list_node

    dummy_head = Node(0, list_node)
    sublist_head = dummy_head

    k = 1
    while k < start:
        sublist_head = sublist_head.next
        k += 1

    # Reverse sublist
    sublist_iter = sublist_head.next
    while start < end:
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp
        start += 1

    return dummy_head.next


def main():
    assert get_list_from_head(reverse_sublist(get_test_list_1(), 1, 3)) == [5, 3, 1]
    assert get_list_from_head(reverse_sublist(get_test_list_1(), 2, 3)) == [1, 5, 3]
    assert get_list_from_head(reverse_sublist(get_test_list_1(), 1, 1)) == [1, 3, 5]
    assert get_list_from_head(reverse_sublist(get_test_list_1(), 3, 3)) == [1, 3, 5]
    assert get_list_from_head(reverse_sublist(get_test_list_2(), 1, 3)) == [6, 4, 2]


if __name__ == '__main__':
    main()
