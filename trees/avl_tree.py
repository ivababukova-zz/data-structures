import math

class Node:
    def __init__(self, data):
       self.data = data
       self.left = None
       self.right = None
       self.height = 1

class AVLTree:

    def insert(self, root, key): 
        new_n = Node(key)
        if not root: 
            return new_n
        else:
            return self._insert(root, new_n)

    def _insert(self, root, n):
        if root.data < n.data:
            if not root.right:
                root.right = n
            else:
                self._insert(root.right, n)
        else:
            if not root.left:
                root.left = n
            else:
                self._insert(root.left, n)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        return self._rebalance(root, n)
    
    def _rebalance(self, n, new_n):
        balance = self.getBalance(n)

        # left subtree of n is bigger than right
        if balance > 1:
            print("left !!!!! ", n.data, " **** ", new_n.data)
            # left left:
            if new_n.data < n.left.data:
                print("left left")
                return self.right_rotate(n)
            # left right:
            else:
                print("left right")
                n.left = self.left_rotate(n.left)
                return self.right_rotate(n)

        # right subtree of n is bigger than left
        elif balance < -1:
            print("right !!!!")
            # right right
            if new_n.data > n.right.data:
                return self.left_rotate(n)
            # right left
            else:
                n.right = self.right_rotate(n.right)
                return self.left_rotate(n)

        return n

    def left_rotate(self, y):
        x = y.right
        T2 = x.left
        x.left = y
        y.right = T2

        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return x

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3

        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        
        return y

    def in_order(self, n):
        if n:
            self.in_order(n.left)
            print(n.data, "   ", n.height)
            self.in_order(n.right)

    def getBalance(self, n):
        return self.getHeight(n.left) - self.getHeight(n.right)

    @staticmethod
    def getHeight(n):
        if not n:
            return 0
        return n.height

t = AVLTree()
root = None
root = t.insert(root, 6)
root = t.insert(root, 4)
root = t.insert(root, 12)
root = t.insert(root, 8)
root = t.insert(root, 20)
root = t.insert(root, 7)
root = t.insert(root, 9)
print(root.data)
t.in_order(root)