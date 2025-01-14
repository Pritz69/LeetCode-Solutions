class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        ans=[]
        a=set()
        b=set()
        d=defaultdict(int)
        c=0
        for i in range(len(A)) :
            a.add(A[i])
            b.add(B[i])
            if b and A[i] in b and d[A[i]]==0 :
                c +=1
                d[A[i]]=1
            if a and B[i] in a and d[B[i]]==0:
                c +=1
                d[B[i]]=1
            ans.append(c)
        return ans
            