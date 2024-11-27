from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSametree(self, q: Optional[TreeNode], p: Optional[TreeNode]) -> bool:
        if not q and not p: return True
        if not q or not p or q.val != p.val: return False
        return self.isSametree(q.right, p.right) and self.isSametree(q.left, p.left)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        return (
            self.isSametree(root, subRoot) or
            self.isSubtree(root.right, subRoot) or
            self.isSubtree(root.left, subRoot)
        )
        

