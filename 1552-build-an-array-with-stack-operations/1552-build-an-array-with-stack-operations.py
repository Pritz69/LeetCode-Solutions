class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        l=[]
        ans=[]
        c=0
        for i in range(1,n+1) :
            l.append(i)
            ans.append("Push")
            c +=1
            if l==target :
                break
            if l[c-1] != target[c-1] :
                l.pop(c-1)
                ans.append("Pop")
                c -=1
        return ans

            