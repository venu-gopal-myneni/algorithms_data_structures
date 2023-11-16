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
        self.tail = None
        self.length = 0
        if seq is not None:
            self.length = len(seq)
            self.head = Node(seq[0])
            cur_node = self.head
            for ele in seq[1:]:
                new_node = Node(ele)
                new_node.previous = cur_node
                cur_node.next = new_node
                cur_node = new_node
            self.tail = cur_node

    def __iter__(self):
        cur_node = self.head
        while cur_node is not None:
            yield cur_node
            cur_node = cur_node.next

    def add_node(self, node: Node, direction: str = "right"):
        if direction == "left":
            self.tail.next = node
            self.tail = node
        elif direction == "right":
            node.next = self.head
            self.head = node
        else:
            raise ValueError(f"direction can take only right or left but {direction} was given")

    def __str__(self):
        out = str(self.head)
        cur_node = self.head
        if cur_node is None:
            return out
        while cur_node.next is not None:
            out = f"{out} <--> {cur_node.next}"
            cur_node = cur_node.next
        return out

    def __repr__(self):
        out = "None"
        for node in self:
            if node.is_head:
                out = f"{node}"
            else:
                out = f"{out} - {node}"
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
    print(repr(ll))
    # print(ll.head)
    # print(ll.head.next.next)
    # print(ll.tail.next)

    for node in ll:
        print(node)

    ll = DoublyLinkedList()
    print(repr(ll))
    for node in ll:
        print(node)
