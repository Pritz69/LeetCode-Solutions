class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d={}
        for x in nums :
            d[x]=d.get(x,0)+1
        l=[]
        c=0
        while c!=len(nums) :
            nl=[]
            for x in d :
                if d[x]>0 :
                    nl.append(x)
                    d[x]-=1
                    c +=1
            l.append(nl)
        return l


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        freq = [0] * (len(nums) + 1)
        ans = []

        for c in nums:
            #frequency of the integer c is greater than or equal to the number of rows in the matrix
            if freq[c] >= len(ans):
                ans.append([])

            # Store the integer in the list corresponding to its current frequency.
            ans[freq[c]].append(c)
            freq[c] += 1

        return ans
