# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        ans=[]
        d=defaultdict(list)
        s=set()
        for x in descriptions :
            d[x[0]].append([x[1],x[2]])
            s.add(x[1])
        r=0
        for x in d.keys() :
            if x not in s :
                r=x
                break
        root=TreeNode(r)
        q=deque()
        q.append(root)
        while q :
            node=q.popleft()
            for x in d[node.val] :
                if x[1]==1 :
                    node.left=TreeNode(x[0])
                    q.append(node.left)
                else :
                    node.right=TreeNode(x[0])
                    q.append(node.right)
        #print(d)
        #print(s)
        return root
