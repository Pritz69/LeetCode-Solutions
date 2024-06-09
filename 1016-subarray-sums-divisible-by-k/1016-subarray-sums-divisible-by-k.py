class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sm=0
        cnt=0
        d=defaultdict(int)
        d[0]=1
        for x in nums :
            sm +=x
            if sm%k in d :
                cnt += d[sm%k]
            d[sm%k] +=1
        return cnt
