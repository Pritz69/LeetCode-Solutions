# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append([root]) 
        while q :
            l=q.pop()
            nl=[]
            for x in l :
                if x.left :
                    nl.append(x.left)
                if x.right :
                    nl.append(x.right)
            if not nl :
                break
            q.append(nl)
        return l[0].val
