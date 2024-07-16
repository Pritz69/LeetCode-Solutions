# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def func(node,path,tar) :
            if not node :
                return []
            if node.val==tar :
                return path
            path.append("L")
            res=func(node.left,path,tar)
            if res :
                return res
            path.pop()
            path.append("R")
            res=func(node.right,path,tar)
            if res :
                return res
            path.pop()
            return []
        spath=func(root,[],startValue)
        dpath=func(root,[],destValue)
        i=0
        while i < min(len(spath),len(dpath)) and spath[i]==dpath[i] :
            i +=1
        res=['U']*len(spath[i:]) + dpath[i:]
        return "".join(res)