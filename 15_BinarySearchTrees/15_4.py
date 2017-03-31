def bst_lca_1(tree, node_1, node_2):
    assert node_1 is not None and node_2 is not None and tree is not None

    p = tree
    s = min(node_1.data, node_2.data)
    b = max(node_1.data, node_2.data)

    while p.data <= b.data and p.data >= s.data:
        if p.data == b.data or p.data == s.data:
            return p
        elif s.data < p.data and p.data < b.data:
            return p
        elif s.data < p.data and b.data < p.data:
            p = p.left
        else:
            p = p.right
    return None


def bst_lca_2(tree, node_1, node_2):
    assert tree is not None and node_1 is not None and node_2 is not None
    p = tree
    s = min(node_1.data, node_2.data)
    b = max(node_1.data, node_2.data)

    # p is outside [s, b]
    while p.data < s.data or p.data > b.data:
        while p < s.data:
            p = p.right
        while p > b.data:
            p = p.left
    # Now, [s .. p .. b]
    return p
