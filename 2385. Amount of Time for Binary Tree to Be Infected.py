# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        l = []
        def ino(r):
            if not r:
                return
            ino(r.left)
            if r.left:
                l.append((r.val, r.left.val))
            if r.right:
                l.append((r.val, r.right.val))
            ino(r.right)
        ino(root)
        d = defaultdict(list)
        for x in l:
            d[x[0]].append(x[1])
            d[x[1]].append(x[0])
        t = 0
        q = deque()
        q.append([start])
        visited = set()
        while q:
            level = q.popleft()
            t += 1
            next_level = []
            for node in level:
                if node not in visited:
                    visited.add(node)
                    for nei in d[node] :
                        if nei !=node and nei not in visited :
                            next_level.append(nei)
            if next_level:
                q.append(next_level)
            #print(next_level)
        return t-1
