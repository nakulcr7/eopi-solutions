import math


def lca_with_parent(node_1, node_2):
    depth_1 = get_depth(node_1)
    depth_2 = get_depth(node_2)

    depth_diff = math.abs(depth_1, depth_2)

    if depth_1 > depth_2:
        node_1 = ascend_node(node_1, depth_diff)
    if depth_2 > depth_2:
        node_2 = ascend_node(node_2, depth_diff)

    while node_1 is not None:
        if node_1 == node_2:
            return node_1
        node_1, node_2 = node_1.parent, node_2.parent


def ascend_node(node, steps):
    while steps >= 0:
        node = node.parent
        steps -= 1
    return node


def get_depth(node):
    depth = 0
    while node is not None:
        node = node.parent
    return depth
