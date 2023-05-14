import collections
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        cache = collections.defaultdict(int)
        def dfs(mask,op) :
            if mask in cache :
                return cache[mask]
            for i in range(len(nums)) :
                for j in range(1+i,len(nums)) :
                    if (1<<i) & mask or (1<<j) & mask :
                        continue
                    newmask = mask | (1<<i) | (1<<j)
                    score = op * math.gcd(nums[i],nums[j])
                    cache[mask] = max(cache[mask], score + dfs(newmask,op+1))
            return cache[mask]
        return dfs(0,1)
