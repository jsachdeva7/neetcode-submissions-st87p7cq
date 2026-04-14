# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subRoot):
            return True
        # At this point, not leaves and so should keep going down tree
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))

    def isSameTree(self, s: Optional[TreeNode], r: Optional[TreeNode]):
        if not s and not r:
            return True
        elif (not s or not r) or (s.val != r.val):
            return False
        return (self.isSameTree(s.left, r.left) and
                self.isSameTree(s.right, r.right))