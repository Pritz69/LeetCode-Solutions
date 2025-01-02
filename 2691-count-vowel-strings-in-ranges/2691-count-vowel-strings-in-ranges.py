class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        l=[]
        for x in words :
            if x[0] in "aeiou" and x[-1] in "aeiou" :
                l.append(1)
            else :
                l.append(0)
        for i in range(1,len(l)) :
            l[i]=l[i-1]+l[i]
        ans=[]
        for x in queries:
            start, end = x
            if start > 0:
                ans.append(l[end] - l[start - 1])
            else:
                ans.append(l[end])
        return ans