class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        l=[]
        for i in range(len(names)) :
            l.append((heights[i],names[i]))
        l.sort(reverse=True)
        ans=[]
        for x in l :
            ans.append(x[1])
        return ans