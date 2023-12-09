# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def ino(node) :
            if not node :
                return 
            ino(node.left)
            l.append(node.val)
            ino(node.right)
        ino(root)
        return l
