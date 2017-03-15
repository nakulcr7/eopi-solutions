class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data


# Helper functions
def list_length(node):
    return len(get_list_from_head(node))


def get_test_list_1():
    node3 = Node(5, None)
    node2 = Node(3, node3)
    node1 = Node(1, node2)
    head = node1
    return head


def get_test_list_2():
    node3 = Node(6, None)
    node2 = Node(4, node3)
    node1 = Node(2, node2)
    head = node1
    return head


def get_list_from_head(node):
    nodes = []
    while node is not None:
        nodes.append(node.data)
        node = node.next
    return nodes
