class BTNode(object):
    """
    Represents a Binary Tree node
    """
    def __init__(self, data, left, right, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data
