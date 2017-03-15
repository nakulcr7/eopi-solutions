from node import *


def merge_sorted_lists(node_1, node_2):
    dummy_head = Node(0, None)
    current = dummy_head
    l1, l2 = node_1, node_2

    while l1 is not None and l2 is not None:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 is not None else l2
    return dummy_head.next


def main():
    list_1 = get_test_list_1()
    list_2 = get_test_list_2()
    print get_list_from_head(merge_sorted_lists(list_1, list_2))


if __name__ == '__main__':
    main()
