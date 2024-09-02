class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        k=k%s
        i=0
        while k > 0 :
            if k==0 or k < chalk[i] :
                break
            else :
                k -= chalk[i]
                i +=1
        return i