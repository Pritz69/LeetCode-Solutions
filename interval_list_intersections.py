class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        a,b=0,0
        l1,l2=len(firstList),len(secondList)
        ans=[]
        while a<l1 and b<l2 :
            s=max(firstList[a][0],secondList[b][0])
            e=min(firstList[a][1],secondList[b][1])
            if s<=e :
                ans.append([s,e])
            if firstList[a][1]<secondList[b][1]:
                a +=1 
            else :
                b +=1 
        return ans
