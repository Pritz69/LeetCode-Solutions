# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        m=float('-inf')
        ans=0
        level=0
        q=deque()
        q.append(root)
        while q :
            level +=1
            s =0
            x=len(q)
            for i in range(x) :
                n = q.popleft()
                s += n.val
                if n.left :
                    q.append(n.left)
                if n.right :
                    q.append(n.right)
            if m<s :
                m=s
                ans=level
        return ans
