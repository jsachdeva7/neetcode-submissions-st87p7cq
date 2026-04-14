# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # need to go to the smallest node (left most leaf), and 
        # then start a counter and go back up incrementing the
        # counter until hitting k
        self.count = 0
        self.result = None

        def helper(node: Optional[TreeNode]):
            if not node or self.result is not None:
                return
            helper(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            helper(node.right)

        helper(root)
        return self.result