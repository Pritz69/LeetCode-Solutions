# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def ino(x,l) :
            if not x :
                l.append("*")
                return
            l.append(x.val)
            ino(x.left,l)
            ino(x.right,l)
        l=[]
        ino(p,l)
        l2=[]
        ino(q,l2)
        #print(l,l2)
        return l==l2
