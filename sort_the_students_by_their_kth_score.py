class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        mp={}
        for row in score :
            mp[row[k]] = row 
        key=sorted(mp.keys(),reverse=True)
        res=[]
        for k in key :
            res.append(mp[k])
        return res
