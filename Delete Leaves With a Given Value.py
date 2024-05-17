# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def rec(node) :
            if not node :
                return
            if not node.left and not node.right and node.val==target :
                return 1
            if node.left :
                if rec(node.left)==1 :
                    node.left=None
                    return rec(node)
            if node.right :
                if rec(node.right)==1 :
                    node.right=None
                    return rec(node)
        
        return None if rec(root)==1 else root
            
