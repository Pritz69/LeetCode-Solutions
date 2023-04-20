# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def bfs(node) :
            q=deque()
            q.append([node,0])
            width=1
            while q :
                width=max(width,q[-1][1]-q[0][1]+1)
                for t in range(len(q)):
                    n,l = q.popleft()
                    if n.left :
                        q.append([n.left,2*l +1])
                    if n.right :
                        q.append([n.right,2*l +2])
            return width
        return bfs(root)
