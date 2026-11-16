# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        def check(node, minimum, maximum):
            if node is None:
               return True
            if node.val <= minimum or node.val >= maximum:
                return False
            if not check(node.left, minimum, node.val):
                return False
            if not check(node.right, node.val, maximum):
                return False
            return True

        return check(root, float('-inf'), float('inf'))
        