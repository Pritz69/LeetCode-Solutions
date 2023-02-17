# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def postorder(root) :
            li=[]
            if root :
                li = postorder(root.left)
                li += postorder(root.right)
                li.append(root.val)
            return li
        l=[]
        l=postorder(root)
        l.sort()
        m=float(inf)
        for i in range(1,len(l)) :
            m=min(m,l[i]-l[i-1])
        return m
        
