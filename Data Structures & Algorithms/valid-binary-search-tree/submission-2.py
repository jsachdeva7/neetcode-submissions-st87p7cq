# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)

    def helper(self, node: Optional[TreeNode], lower=float('-inf'), upper=float('inf')) -> bool:
        if not node:
            return True
        val = node.val
        if val <= lower or val >= upper:
            return False

        # left subtree must be < current node
        if not self.helper(node.left, lower, val):
            return False

        # right subtree must be > current node
        if not self.helper(node.right, val, upper):
            return False
        return True
        