# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        q = deque([root])  
        level_sums = []
        while q:
            level_size = len(q)
            level_sum = 0
            for _ in range(level_size):
                node = q.popleft()
                if node:
                    level_sum += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            level_sums.append(level_sum)
        level_sums.sort(reverse=True)
        if k > len(level_sums):
            return -1
        return level_sums[k - 1]