# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        li=[]
        def rec(root) :
            if not root :
                return (0,0)
            l=rec(root.left)
            r=rec(root.right)
            sum=l[0]+r[0]+root.val
            cnt=l[1]+r[1]+1
            if sum//cnt == root.val :
                li.append(root.val)
            return (sum,cnt)
        rec(root)
        #print(li)
        return len(li)