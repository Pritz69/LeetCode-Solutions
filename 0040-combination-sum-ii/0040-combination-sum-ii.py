class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def rec(start, s, p):
            if s == target:
                ans.append(p)
                return
            if s > target:
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                rec(i + 1, s + candidates[i], p + [candidates[i]])
        candidates.sort()
        ans = []
        rec(0, 0, [])
        return ans
