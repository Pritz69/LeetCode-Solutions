# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q=deque([root])
        while q :
            node=q.popleft()
            if node :
                q.append(node.left)
                q.append(node.right)
            else :
                while q :
                    if q.popleft() :
                        return False
        return True
