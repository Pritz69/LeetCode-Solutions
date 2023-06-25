class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp={}
        def dfs(start,fuel) :
            if fuel<0 :
                return 0
            if (start,fuel) in dp :
                return dp[(start,fuel)]
            c = 0 
            if start==finish :
                c = 1
            for i in range(len(locations)) :
                if i!=start :
                    c += dfs(i,fuel-abs(locations[i]-locations[start])) 
            dp[(start,fuel)] = c
            return c % (10**9 + 7)
        return dfs(start,fuel)
        
