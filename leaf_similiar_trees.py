# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def construct(root):
            arr=[]
            def traverse(node):
                if node is None :
                    return 
                traverse(node.left)
                if node.left is None and node.right is None :
                    arr.append(node.val)
                traverse(node.right)
            traverse(root)
            return arr
        return construct(root1)==construct(root2)
