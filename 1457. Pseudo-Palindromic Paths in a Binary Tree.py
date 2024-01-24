# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def isvalid(d):
            f=0
            for x in d :
                if d[x]%2 ==1 : #odd freq must be 1 for a palindromic sequence
                    f +=1
                if f>1 :
                    return False
            return True
        def rec(node,d) :
            nonlocal c
            if not node :
                return 
            d[node.val] +=1
            if not node.left and not node.right :
                if isvalid(d) :
                    #print(d)
                    c +=1
            if node.left :
                rec(node.left,d.copy())
            if node.right :
                rec(node.right,d.copy())
            d[node.val] -=1
        c=0
        d=defaultdict(int)
        rec(root,d)
        return c
