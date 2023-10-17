class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def findroot() :
            s={}
            for i in leftChild :
                if i!=-1 :
                    s[i]=s.get(0,1)
            for i in rightChild :
                if i!=-1 :
                    s[i]=s.get(0,1) + 1
            for i in range(n) :
                if i not in s :             # Root has no parent, so must not be present in any children list
                    return i
            return -1

        root=findroot()
        if root==-1 :
            return False
        
        seen={root}
        stack=[root] 
        while stack :
            node = stack.pop()
            for children in [leftChild[node],rightChild[node]] :
                if children != -1 :
                    if children in seen :
                        return False
                    seen.add(children)
                    stack.append(children)
        return len(seen)==n