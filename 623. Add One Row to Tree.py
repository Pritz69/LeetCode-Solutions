# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def func(root,val,level):
            if not root :
                return
            if depth==1 :
                node=TreeNode(val)
                node.left=root
                return node
            if level==depth-1 :
                node=TreeNode(val)
                node.left=root.left
                root.left=node
                node2=TreeNode(val)
                node2.right=root.right
                root.right=node2  
            else :
                func(root.left,val,level+1)
                func(root.right,val,level+1)
            return root
        return func(root,val,1)
