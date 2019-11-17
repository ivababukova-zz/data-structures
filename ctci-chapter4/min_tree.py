class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class MinimalBST:

    def __init__(self, A):
        self.root = self._insert_midd(A)

    def _insert_midd(self, A):
        if len(A) == 0:
            return
        middle = int(len(A)/2)
        n = Node(A[middle])
        n.left = self._insert_midd(A[:middle])
        n.right = self._insert_midd(A[middle+1:])
        return n


    def insert(self, data):
        self._insert(self.root, data)

    def _insert(self, root, data):
        if data >= root.data:
            if not root.right:
                root.right = Node(data)
            else:
                self._insert(root.right, data)

        elif data < root.data:
            if not root.left:
                root.left = Node(data)
            else:
                self._insert(root.left, data)

    def in_order(self):
        self._in_order(self.root)

    def _in_order(self, root):
        if root:
            self._in_order(root.left)
            print(root.data)
            self._in_order(root.right)



A = [2, 8, 9, 15, 20, 25, 27]

t = MinimalBST(A)
t.in_order()