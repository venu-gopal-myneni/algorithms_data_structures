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
            tag = "(Single)"
        elif self.is_head:
            tag = "(Head)"
        elif self.is_tail:
            tag = "(Tail)"
        else:
            tag = ""
        return f"{tag} {self.data}"


class DoublyLinkedList:
    def __init__(self, seq=None):  # [1,2,3,4,5]
        self.head = None
        if seq is not None:
            self.head = Node(seq[0])
            cur_node = self.head
            for ele in seq[1:]:
                new_node = Node(ele)
                new_node.previous = cur_node
                cur_node.next = new_node
                cur_node = new_node

    def __str__(self):
        out = str(self.head)
        cur_node = self.head
        while cur_node.next is not None:
            out = f"{out} -> {cur_node.next}"
            cur_node = cur_node.next
        return out


if __name__ == "__main__":
    node1 = Node(5)
    node3 = Node(10)
    node2 = Node(7, node1, node3)

    print(node1)
    print(node2)
    print(node3)

    ll = DoublyLinkedList([23, 12, 45, 67, 100])
    print(ll)
