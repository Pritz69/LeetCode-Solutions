# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        l=[]
        def preorder(root) :
            if not root :
                return
            preorder(root.left)
            l.append(root.val)
            preorder(root.right)
        preorder(root)
        m = float('inf')
        for i in range(1,len(l)) :
            m = min(m,abs(l[i]-l[i-1]))
        return m
