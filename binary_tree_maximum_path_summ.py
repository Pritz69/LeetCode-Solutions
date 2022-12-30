# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]
        def dfs(root) :
            if not root :
                return 0
            lftmax=dfs(root.left)
            rhtmax=dfs(root.right)
            lftmax=max(lftmax,0)
            rhtmax=max(rhtmax,0)
            res[0]=max(res[0],lftmax+rhtmax+root.val)
            return root.val + max(lftmax,rhtmax)
        dfs(root)
        return res[0]
        
