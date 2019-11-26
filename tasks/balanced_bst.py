"""
https://leetcode.com/discuss/interview-question/413991/

Design a tree-based data structure to efficiently manipulate a very long string.

class LongString {

	public LongString(String s) {
		// todo
	}
	
	/**
	* Returns the character at position 'i'.
	*/
	public char charAt(int i) {
		// todo
	}

	/**
	* Deletes the specified character substring.
	* The substring begins at the specified 'start' and extends to the character at index 'end - 1' or to the end of the sequence
	* if no such character exists.
	* If 'start' is equal to 'end', no changes are made.
	*
	* @param      start  The beginning index, inclusive.
	* @param      end    The ending index, exclusive.
	* @throws     StringIndexOutOfBoundsException  if 'start' is negative, greater than length, or greater than 'end'.
	*/
	public void delete(int start, int end) {
		// todo
	}
}
"""

class Node:

    def __init__(self, i, s, left=None, right=None):
        self.index = i
        self.data = s
        self.left = left
        self.right = right
        self.height = 1

    def __repr__(self):
        return "{}:{}".format(self.index, self.data)

class BalancedBST:

    def insert_str(self, st, root):
        for i, s in enumerate(st):
            root = self.insert(root, i, s)
        return root
    
    def insert(self, root, i, s):
        if not root: 
            return Node(i, s) 
        elif i < root.index: 
            root.left = self.insert(root.left, i, s) 
        else: 
            root.right = self.insert(root.right, i, s)
        
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.rebalance(root, i)

    def rebalance(self, root, index):
        balance = self.get_balance(root)
        if balance > 1:
            # left left
            if index < root.left.index:
                return self._rotate_right(root)
            # left right
            else:
                root.left = self._rotate_left(root.left)
                return self._rotate_right(root)
        if balance < -1:
            # right right
            if index > root.right.index:
                return self._rotate_left(root)
            # right left
            else:
                root.right = self._rotate_right(root.right)
                return self._rotate_left(root)

        return root

    def _rotate_left(self, y):
        x = y.right
        y.right = x.left
        x.left = y

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def _rotate_right(self, z):
        y = z.left
        z.left = y.right
        y.right = z

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))

        return y

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.index, root.data, root.height)
            self.in_order(root.right)

    def get_height(self, n):
        if not n:
            return 0
        return n.height

    def get_balance(self, n):
        return self.get_height(n.left) - self.get_height(n.right)

    def get_char_at(self, index, root):
        print("****")
        if not root:
            return -1
        if index == root.index:
            return root.data
        if index > root.index:
            return self.get_char_at(index, root.right)
        elif index < root.index:
            return self.get_char_at(index, root.left)
    
    def delete_substring(self, start_i, end_i, root):




st = "helloiva"
t = BalancedBST()
# root = None
# root = t.insert_str(st, root)
# t.in_order(root)
# c = t.get_char_at(3, root)
# print(c)
