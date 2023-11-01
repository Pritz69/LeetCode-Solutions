# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def inorder(root) :
            if not root :
                return 
            if root.left :
                inorder(root.left)
            l.append(root.val)
            if root.right :
                inorder(root.right)
        inorder(root)
        d={}
        for x in l :
            d[x]=d.get(x,0)+1
        m,v=0,0
        for x in d :
            if d[x] > m :
                m=d[x]
        ans=[]
        for x in d :
            if d[x]==m :
                ans.append(x)
        return ans