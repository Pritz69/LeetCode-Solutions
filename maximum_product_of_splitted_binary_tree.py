# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        m=10**9 + 7
        def dfs(node):
            if node is None :
                return 0
            return node.val + dfs(node.left) +dfs(node.right)
        t=dfs(root)
        best=0
        def traverse(node):
            if node is None :
                return 0
            a=node.val+traverse(node.left)+traverse(node.right)
            b=t-a
            nonlocal best
            best=max(best,a*b)
            return a
        traverse(root)
        return best%m
