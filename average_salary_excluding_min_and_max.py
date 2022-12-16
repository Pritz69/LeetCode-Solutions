class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n=len(salary)-2
        s=0
        for i in range(1,len(salary)-1):
            s += salary[i]
        return (s/n)
