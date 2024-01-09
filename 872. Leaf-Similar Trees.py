# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1=[]
        l2=[]
        def ino(root,l) :
            if root is None :
                return
            ino(root.left,l)
            if root.left is None and root.right is None :
                l.append(root.val)
            ino(root.right,l)
        ino(root1,l1)
        ino(root2,l2)
        return l1==l2
