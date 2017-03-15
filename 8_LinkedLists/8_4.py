from node import *


def overlapping_no_cycle_lists(list_1, list_2):
    len_l1 = list_length(list_1)
    len_l2 = list_length(list_2)

    if len_l1 > len_l2:
        list_1 = advance_list_by_k(list_1, len_l1 - len_l2)
    else:
        list_2 = advance_list_by_k(list_2, len_l2 - len_l1)

    while list_1 is not None and list_2 is not None and list_1 != list_2:
        list_1 = list_1.next
        list_2 = list_2.next
    return list_1


def advance_list_by_k(l, k):
    while k >= 0:
        l = l.next
    return l
