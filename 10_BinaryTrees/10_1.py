import math


class BalancedStatusWithHeight(object):
    def __init__(self, balanced, height):
        self.balanced = balanced
        self.height = height


def is_balanced(tree):
    return check_balanced(tree).balanced


def check_balanced(tree):
    if tree is None:
        return BalancedStatusWithHeight(True, -1)
    left_result = check_balanced(tree.left)
    if not left_result.balanced:
        return left_result
    right_result = check_balanced(tree.right)
    if not right_result.balanced:
        return right_result
    is_balanced = math.abs(left_result.height - right_result.height) <= 1
    height = max(left_result.height, right_result.height) + 1
    return BalancedStatusWithHeight(is_balanced, height)
