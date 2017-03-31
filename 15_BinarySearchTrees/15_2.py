def find_first_greater_than_k(tree, k):
    subtree = tree
    first_so_far = None

    while subtree is not None:
        if subtree.data > k:
            first_so_far = subtree
            subtree = subtree.left
        else:
            subtree = subtree.right
    return first_so_far
