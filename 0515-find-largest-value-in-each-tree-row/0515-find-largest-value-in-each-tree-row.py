# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root==None :
            return []
        q=deque()
        q.append([root])
        ans=[]
        while q :
            n=q.popleft()
            ans.append(max([x.val for x in n]))
            l=[]
            for x in n :
                if x.left :
                    l.append(x.left)
                if x.right :
                    l.append(x.right)
            if l :
                q.append(l)
        return ans