# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans=[]
        def func(node,s) :
            nonlocal ans
            if not node :
                return
            s=s+chr(node.val+97)
            if not node.left and not node.right :
                s=s[::-1]
                if not ans :
                    ans.append(s)
                else :
                    ans[0]=min(ans[0],s)
                return 
            func(node.left,s)
            func(node.right,s)
        func(root,"")   
        return ans[0]
