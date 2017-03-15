def search(node, key):
    while node is not None and node.data != key:
        node = node.next
    return node


def insert_after(node, new_node):
    new_node.next = node.next
    node.next - new_node.next


def delete_node_after(node):
    node.next = node.next.next
