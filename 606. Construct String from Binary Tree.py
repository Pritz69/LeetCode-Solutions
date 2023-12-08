# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def func(root) :
            nonlocal st
            if not root :
                return
            st+=str(root.val)
            if root.left or root.right : 
                st+="("
                func(root.left)
                st+=")"
            if root.right :
                st+="("
                func(root.right)
                st+=")"
        st=""
        func(root)
        return st
