# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {}
        self.root = None
        self.pre_idx = 0

        for i in range(len(inorder)):
            root_val = inorder[i]
            indexMap[root_val] = i

        
        def helper(left, right):
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1

            root = TreeNode(root_val)

            inorder_index = indexMap[root_val]

            root.left = helper(left, inorder_index - 1)
            root.right = helper(inorder_index + 1, right)

            return root

        return helper(0, len(inorder) - 1)