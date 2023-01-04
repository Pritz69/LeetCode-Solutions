class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        c=Counter(tasks)
        f=0
        for i in c :
            if c[i]==1:
                return -1
            elif c[i]%3 ==0 :
                f +=c[i]//3 
            else :
                f +=c[i]//3 +1
        return f
