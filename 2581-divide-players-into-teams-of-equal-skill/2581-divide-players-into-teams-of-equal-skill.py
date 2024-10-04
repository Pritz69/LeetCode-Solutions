class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        a=skill[0]+skill[-1]
        for i in range(1,len(skill)) :
            if skill[i]+skill[len(skill)-i-1] != a :
                return -1
        ans=0
        for i in range(len(skill)) :
            ans += (skill[i]*skill[len(skill)-i-1])
        return ans//2