class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans=""
        j=0
        for i in range(len(s)):
            if j<len(spaces) and i!=spaces[j] :
                ans+=s[i]
            else :
                if j==len(spaces) :
                    ans +=s[i]
                else :
                    ans+=" "
                    ans+=s[i]
                    j +=1
        return ans