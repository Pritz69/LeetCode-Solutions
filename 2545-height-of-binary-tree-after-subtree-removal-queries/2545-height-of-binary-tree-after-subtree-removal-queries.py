# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root, queries, ans = {}) -> List[int]:
        @cache
        def height(r): return 1 + max(height(r.left), height(r.right)) if r else 0
        def dfs(r, depth, mx):
            if not r: return
            ans[r.val] = mx
            dfs(r.left, depth + 1, max(mx, depth + height(r.right)))
            dfs(r.right, depth + 1, max(mx, depth + height(r.left)))
        dfs(root, 0, 0)
        return [ans[v] for v in queries]