class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr=[]
        for i,x in enumerate(score) :
            arr.append((i,x))
        arr.sort(key=lambda x:x[1],reverse=True)
        ans=[0]*(len(arr))
        for i in range(len(arr)):
            if i==0 :
                ans[arr[i][0]]="Gold Medal"
            elif i==1 :
                ans[arr[i][0]]="Silver Medal"
            elif i==2 :
                ans[arr[i][0]]="Bronze Medal"
            else :
                ans[arr[i][0]]=str(i+1)
        return ans
