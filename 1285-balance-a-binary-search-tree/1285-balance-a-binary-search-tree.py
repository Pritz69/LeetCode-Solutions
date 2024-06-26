# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        li=[]
        def inorder(node) :
            if not node :
                return 
            inorder(node.left)
            li.append(node.val)
            inorder(node.right)
        inorder(root)
        def helper(l,r,li) :
            if l>r :
                return
            m=(l+r)//2
            root=TreeNode(li[m])
            root.left=helper(l,m-1,li)
            root.right=helper(m+1,r,li)
            return root
        return helper(0,len(li)-1,li)