class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count=collections.defaultdict(int)
        total,res,l=0,0,0
        for r in range (len(fruits)) :
            count[fruits[r]] +=1
            total +=1

            while len(count) > 2 :
                count[fruits[l]] -=1
                total -=1
                if not count[fruits[l]] :
                    count.pop(fruits[l])
                l +=1
            res = max(res,total)
        return res