# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        def lheight(root):
            if not root:
                return 0
            return 1 + lheight(root.left)
        def rheight(root):
            if not root:
                return 0
            return 1+ rheight(root.right)
        l,r=lheight(root),rheight(root)
        if l>r :
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        else :
            return (2**l)-1

        
