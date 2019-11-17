class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1

class BinarySearchTree:

    def __init__(self, data):
        self.root = Node(data)
        self.depths = {}

    def insert(self, data, root=None):
        if not root:
            root = self.root
        if data > root.data:
            if not root.right:
                root.right = Node(data)
            else:
                self.insert(data, root.right)
        elif data < root.data:
            if not root.left:
                root.left = Node(data)
            else:
                self.insert(data, root.left)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, root):
        if root:
            self._in_order(root.left)
            print(root.data)
            self._in_order(root.right)

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def is_balanced(self):
        root_balance = self.get_balance(self.root)
        return -1 < root_balance < 1

    def get_balance(self, n):
        return self.get_height(n.left) - self.get_height(n.right)

t = BinarySearchTree(6)
t.insert(10)
t.insert(3)
t.insert(8)
t.insert(7)
t.in_order()
print(t.is_balanced())