class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        s=set()
        m=0
        for x in arr1 :
            x=str(x)
            for i in range(len(x)) :
                s.add(x[:i+1])
        for x in arr2 :
            x=str(x)
            for i in range(len(x)) :
                if x[:i+1] in s :
                    m=max(m,i+1)
        return m