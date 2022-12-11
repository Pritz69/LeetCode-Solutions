# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0, float("-inf") 
            left, wl = dfs(root.left)
            left = max(left,0)
            
            right, wr = dfs(root.right)
            right = max(right,0)
            
            res = max(wl, wr, root.val+left+right)
            return  root.val+max(left,right) ,res

        return dfs(root)[1]
