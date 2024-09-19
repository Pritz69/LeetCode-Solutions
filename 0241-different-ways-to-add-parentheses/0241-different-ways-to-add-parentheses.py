class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operations={
            "+" : lambda x,y : x+y,
            "-" : lambda x,y : x-y,
            "*" : lambda x,y : x*y
        }
        def dfs(l,r) :
            res=[]
            for i in range(l,r+1) :
                op=expression[i]
                if op in operations :
                    n1=dfs(l,i-1)
                    n2=dfs(i+1,r)
                    for x in n1 :
                        for y in n2 :
                            res.append(operations[op](x,y))
            if res==[]:
                res.append(int(expression[l:r+1]))
            return res
        return dfs(0,len(expression)-1)