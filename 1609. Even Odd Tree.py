# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q=deque()
        q.append([root])
        c=-1
        while q :
            l=q.pop()
            c +=1
            nl=[]
            f=0
            if c%2==0 :
                if len(l)==1 :
                    if l[0].val%2==0 :
                        return 0
                for i in range(len(l)-1) :
                    if l[i+1].val <= l[i].val  :
                        f=1
                        return 0
                    if l[i].val%2==0 or l[i+1].val%2==0 :
                        f=1
                        return 0
            else :
                if len(l)==1 :
                    if l[0].val%2==1 :
                        return 0 
                for i in range(len(l)-1) :
                    if l[i+1].val >= l[i].val  :
                        f=1
                        return 0
                    if l[i].val %2==1 or l[i+1].val %2==1 :
                        f=1
                        return 0
            if f==0 :
                for x in l :
                    if x.left :
                        nl.append(x.left)
                    if x.right :
                        nl.append(x.right)
            if not nl :
                break
            q.append(nl)
        return 1
