class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, root):
        if root:
            self._in_order(root.left)
            print(root.data)
            self._in_order(root.right)

    def get_list_depths(self):
        self.root.depth = 1
        self.traverse(self.root)
        for depth in self.depths.keys():
            print(depth, " * ", [n.data for n in self.depths[depth]])

    def traverse(self, n):
        if n.depth not in self.depths:
            self.depths[n.depth] = []
        self.depths[n.depth].append(n)
        if n.left:
            n.left.depth = n.depth + 1
            self.traverse(n.left)
        if n.right:
            n.right.depth = n.depth + 1
            self.traverse(n.right)


t = BinarySearchTree(6)
t.insert(10)
t.insert(3)
t.insert(1)
t.insert(8)
t.in_order()
t.get_list_depths()