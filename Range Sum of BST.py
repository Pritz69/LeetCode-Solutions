# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s=0
        def ino(root) :
            nonlocal s
            if not root :
                return
            ino(root.left)
            if low <= root.val <= high :
                s +=root.val
            ino(root.right)
        ino(root)
        return s
