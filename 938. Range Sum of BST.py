# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        total=0

        def myfunc(root):
            nonlocal total
            if not root:
                return 
            if root.val >= low and root.val<=high:
                total+=root.val
            if root.val<high:
                myfunc(root.right)
            if root.val>low:
                myfunc(root.left)
        myfunc(root)
        return total
        