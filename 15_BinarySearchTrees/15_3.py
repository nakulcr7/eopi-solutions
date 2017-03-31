def find_k_largest_elements(tree, k):
    return find_k_largest_elements_helper(tree, k, list())


def find_k_largest_elements_helper(node, k, results):
    if node is not None and len(results) <= k:
        results = find_k_largest_elements_helper(node.right, k, results)
        results.append(node.data)
        results = find_k_largest_elements_helper(node.left, k, results)
    return results
