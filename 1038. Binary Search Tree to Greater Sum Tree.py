# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total=0

        def sumtree(root):
            nonlocal total
            if not root:
                return
            sumtree(root.right)
            total+=root.val
            root.val=total
            sumtree(root.left)
        sumtree(root)
        return root




        