class BinaryTree():
    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    # get methods
    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_root_val(self):
        return self.root

    # set methods
    def set_root_val(self, val):
        self.root = val

    def insert_left(self, val):
        if self.get_left_child() is None:
            self.left_child = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.left_child = self.get_left_child()
            self.left_child = t

    def insert_right(self, val):
        if self.get_right_child() is None:
            self.right_child = BinaryTree(val)
        else:
            t = BinaryTree(val)
            t.right_child = self.get_right_child()
            self.right_child = t

    def print_me(self):
        print(self.get_root_val())
        if self.get_left_child() is not None:
            lefty = self.get_left_child().get_root_val()
        else:
            lefty = "xx"

        if self.get_right_child() is not None:
            rity = self.get_right_child().get_root_val()
        else:
            rity = "xx"

        print(
            f" {lefty}       {rity}")


def pre_order_traversal(tree):
    if tree is not None:
        print(tree.get_root_val())
        pre_order_traversal(tree.get_left_child())
        pre_order_traversal(tree.get_right_child())


def in_order_traversal(tree):
    if tree is not None:
        in_order_traversal(tree.get_left_child())
        print(tree.get_root_val())
        in_order_traversal(tree.get_right_child())


def post_order_traversal(tree):
    if tree is not None:
        post_order_traversal(tree.get_left_child())
        post_order_traversal(tree.get_right_child())
        print(tree.get_root_val())


class BinaryHeap():
    def __init__(self):
        self.list = []

    def insert(self, num):
        if len(self.list) == 0:
            self.list.append(num)
        else:
            self.list.append(num)
            self.perc_up(len(self.list))

    def perc_up(self, size):
        while (size//2 - 1) >= 0:
            if self.list[size//2 - 1] < self.list[size-1]:
                temp = self.list[size//2 - 1]
                self.list[size//2 - 1] = self.list[size-1]
                self.list[size-1] = temp
            else:
                break

            size = size//2

    def max_child(self):
        if len(self.list) > 0:
            return self.list[0]
        else:
            raise "Empty Heap"

    def get_max_child_pos(self, pos):
        pos1 = 2*pos + 1
        item1 = self.list[2*pos + 1]

        pos2 = 2*pos + 2
        item2 = None
        if (2*pos + 2) <= len(self.list)-1:
            item2 = self.list[2*pos + 2]

        if item2 is None:
            return pos1
        else:
            if item1 > item2:
                return pos1
            else:
                return pos2

    def perc_down(self):
        self.list[0] = self.list[-1]
        self.list = self.list[0:-1]
        cur_pos = 0
        while (2*cur_pos + 1) <= len(self.list)-1:
            max_child_pos = self.get_max_child_pos(cur_pos)
            if self.list[max_child_pos] > self.list[cur_pos]:
                temp = self.list[cur_pos]
                self.list[cur_pos] = self.list[max_child_pos]
                self.list[max_child_pos] = temp
                cur_pos = max_child_pos
            # elif (2*cur_pos + 2) <= len(self.list)-1:
            #     if self.list[2*cur_pos + 2] > self.list[cur_pos]:
            #         temp = self.list[cur_pos]
            #         self.list[cur_pos] = self.list[2*cur_pos + 2]
            #         self.list[2*cur_pos + 2] = temp
            #         cur_pos = 2*cur_pos + 2
            else:
                break

    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            out = self.list[0]
            self.perc_down()
            return out

    def __str__(self):
        return f"{self.list}"


class TreeNode():
    def __init__(self, key, val, left=None, right=None, parent=None) -> None:
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.left_child or self.right_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.left_child = lc
        self.right_child = rc
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self


class Node():
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = Node(value)
            else:
                self._insert(value, cur_node.left_child)
        else:
            if cur_node.right_child is None:
                cur_node.right_child = Node(value)
            else:
                self._insert(value, cur_node.right_child)

    def _print_tree(self, cur_node):
        # in order
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print(f"{cur_node.value}")
            self._print_tree(cur_node.right_child)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
        else:
            print("Empty Tree.")

    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root, 0)

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        else:
            left_height = self._height(cur_node.left_child, cur_height+1)
            right_height = self._height(cur_node.right_child, cur_height+1)
            return max(left_height, right_height)

    def search(self, value):
        if self.root is None:
            return False
        else:
            return self._search(value, self.root)

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._search(value, cur_node.right_child)
        else:
            return False


if __name__ == "__main__":

    bst = BinarySearchTree()
    alist = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    alist = [-10, 20, 500, 1234, 5000, 10000, 120000]
    for i in alist:
        bst.insert(i)
    bst.print_tree()
    print(bst.height())
    print(bst.search(0.001))
    # r = BinaryHeap()
    # # r.max_child()
    # r.insert(5)
    # print(r)
    # r.insert(7)
    # print(r)
    # r.insert(3)
    # print(r)
    # r.insert(11)
    # print(r)
    # r.insert(9)
    # print(r)
    # r.insert(22)
    # print(r)
    # r.insert(12)
    # print(r)
    # r.pop()
    # print(r)
    # r.pop()
    # print(r)
    # r.pop()
    # print(r)
    # r.pop()
    # print(r)

    # r = BinaryTree("a")
    # r.insert_left('b')
    # r.get_left_child().insert_left("d")
    # r.get_left_child().insert_right("e")
    # r.get_left_child().get_left_child().insert_left("h")
    # r.get_left_child().get_left_child().insert_right("i")
    # r.insert_right('c')
    # r.get_right_child().insert_left("f")
    # r.get_right_child().insert_right("g")
    # r.get_right_child().get_right_child().insert_left("j")

    # pre_order_traversal(r)
    # in_order_traversal(r)
    # post_order_traversal(r)
