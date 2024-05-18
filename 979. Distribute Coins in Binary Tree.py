# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans=0
        def rec(node) :
            nonlocal ans
            if not node :
                return 0
            l=rec(node.left)
            r=rec(node.right)
            ans += abs(l) + abs(r)
            return node.val + l + r - 1
        rec(root)
        return ans
