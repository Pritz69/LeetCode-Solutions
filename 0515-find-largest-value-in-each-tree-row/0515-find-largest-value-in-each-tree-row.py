# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        q=deque()
        q.append(root)
        while q :
            m=float('-inf')
            for i in range(len(q)) :
                v=q.popleft()
                if v :
                    m=max(m,v.val)
                    q.append(v.left)
                    q.append(v.right)
            if q :
                ans.append(m)
        return ans