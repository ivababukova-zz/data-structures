# task: https://leetcode.com/discuss/interview-question/350363/Google-or-OA-2018-or-Max-Distance

# The distance between 2 binary strings is the sum of their lengths after removing the common prefix.
# For example: the common prefix of 1011000 and 1011110 is 1011 so the distance is len("000") + len("110") = 3 + 3 = 6.
# Given a list of binary strings, pick a pair that gives you maximum distance among all possible pair and return that distance.

NODE_CLASSIFICATIONS = ["root", "leaf", "middle"]

class Node:

    def __init__(self, marked=False):
        self.left = None
        self.right = None
        self.marked = marked 

def find_max_distance(arr):

    def create_tree(arr):
        root = Node()
        for st in arr:
            L = len(st)
            node = root
            for i in range(L):
                if st[i] == "0":
                    if not node.left:
                        node.left = Node()
                    node = node.left
                else:
                    if not node.right:
                        node.right = Node()
                    node = node.right
            node.marked = True
        return root

    root = create_tree(arr)
    def max_distance(node, maxi):
        if not node:
            return 0, 0
        left_max_sum, left_height = max_distance(node.left, maxi)
        right_max_sum, right_height = max_distance(node.right, maxi)
        
        max_sum = max(left_max_sum, right_max_sum)
        if node.marked or (node.left and node.right):
            max_sum = max(max_sum, left_height + right_height)

        height = max(left_height, right_height) + 1

        return max_sum, height

    distance, _ = max_distance(root, 0)
    print(distance)
    return distance

arr = ["1011000", "1011110", "11101", "1001", "10101", "01"]
find_max_distance(arr)