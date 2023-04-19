# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        def dfs(node,dir,len) :
            if node==None :
                return 
            self.maxi=max(self.maxi,len)
            if dir==0 :
                dfs(node.left,0,1)
                dfs(node.right,1,len+1)
            else :
                dfs(node.right,1,1)
                dfs(node.left,0,len+1)
            return 
        dfs(root.left,0,1)
        dfs(root.right,1,1)
        return self.maxi
