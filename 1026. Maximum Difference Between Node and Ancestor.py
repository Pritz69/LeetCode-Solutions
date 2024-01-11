# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def ino(r) :
            nonlocal m
            if not r :
                return 0
            if r.left and r.right :
                mil,mal=ino(r.left)
                mir,mar=ino(r.right)
                m=max(m,abs(r.val-mil),abs(r.val-mir))
                m=max(m,abs(r.val-mal),abs(r.val-mar))
                return min(mil,r.val,mir),max(mal,r.val,mar)
            if r.left :
                mi,ma=ino(r.left)
                m=max(m,abs(r.val-mi))
                m=max(m,abs(r.val-ma))
                return min(mi,r.val),max(ma,r.val)
            if r.right :
                mi,ma=ino(r.right)
                m=max(m,abs(r.val-mi))
                m=max(m,abs(r.val-ma))
                return min(mi,r.val),max(ma,r.val)
            return r.val,r.val
        m=0
        ino(root)
        return m
        
#[2,null,0,null,4,null,3,null,1]
#[2,5,0,null,null,4,null,null,6,1,null,3]
