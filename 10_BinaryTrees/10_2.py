def is_symmetric(tree):
    return True if tree is None else check_symmetric(tree.left, tree.right)


def check_symmetric(tree_1, tree_2):
    if tree_1 is None and tree_2 is None:
        return True
    elif tree_1 is not None and tree_2 is not None:
        return tree_1 == tree_2 and \
            check_symmetric(tree_1.left, tree_1.right) and \
            check_symmetric(tree_2.left, tree_2.right)
    else:
        return False
