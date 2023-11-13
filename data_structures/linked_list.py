class Node:
    def __init__(self, data=None, previous_node=None, next_node=None):
        self.data = data
        self.previous = previous_node
        self.next = next_node

    @property
    def is_head(self):
        if self.previous is None:
            return True
        return False

    @property
    def is_tail(self):
        if self.next is None:
            return True
        return False

    def __str__(self):
        if self.is_head and self.is_tail:
            tag = "Single"
        elif self.is_head:
            tag = "Head"
        elif self.is_tail:
            tag = "Tail"
        else:
            tag = ""
        return f"{tag} {self.data}"


if __name__ == "__main__":
    node1 = Node(5)
    node3 = Node(10)
    node2 = Node(7, node1, node3)

    print(node1)
    print(node2)
    print(node3)
