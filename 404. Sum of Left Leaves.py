# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans=0
        def inorder(node) :
            nonlocal ans
            if not node :
                return
            if node.left :
                if not node.left.left and not node.left.right :
                    ans += node.left.val 
                inorder(node.left)
            if node.right :
                inorder(node.right)
        inorder(root)
        return ans 
