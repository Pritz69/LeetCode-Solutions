# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def rec(node) :
            if not node :
                return 
            if node.val==3 :
                return rec(node.left) & rec(node.right)
            elif node.val==2 :
                return rec(node.left) | rec(node.right)
            else :
                return node.val
        
        return rec(root)
