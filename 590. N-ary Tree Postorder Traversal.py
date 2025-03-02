"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return

        result=[]
        def myfunc(root):
            for child in root.children:
                myfunc(child)
            result.append(root.val)
        myfunc(root)
        return result
        


        

        


        