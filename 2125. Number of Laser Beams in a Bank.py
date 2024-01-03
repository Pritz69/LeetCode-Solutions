class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        c=0
        i=0
        n=len(bank)
        while i < n :
            cnt=bank[i].count('1')
            j=i+1
            while j<n and bank[j].count('1') ==0 :
                j +=1
            if j<n :
                cnt2=bank[j].count('1')
                c += cnt*cnt2
            i=j
        return c
