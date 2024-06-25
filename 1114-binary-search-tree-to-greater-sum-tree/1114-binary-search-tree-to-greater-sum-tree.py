# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        l=[]
        def inorder(node) :
            if not node :
                return 
            inorder(node.left)
            l.append(node.val)
            inorder(node.right)
        def changer(node) :
            if not node :
                return
            changer(node.left)
            s=0
            for x in l :
                if x >= node.val :
                    s +=x
            node.val=s
            changer(node.right)
        inorder(root)
        changer(root)
        return root
        