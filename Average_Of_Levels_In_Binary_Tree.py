# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS solution
        queue = []  # we use first in first out quene for Breadth-First-search
        result = []
        queue.append(root)
        
        while(queue):   # loop through every level
            qlen = len(queue)   # how many elements in the current row
            tmp = 0
            for i in range(qlen):   # loop through elements in current level
                node = queue.pop(0)
                tmp += node.val
                if node.left:   
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tmp/qlen)    # calculate the average 
        
        return result
