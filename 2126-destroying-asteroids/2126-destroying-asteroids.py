class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        if asteroids[0] > mass :
            return False
        #print(asteroids)
        f=0
        for i in range(len(asteroids)) :
            if asteroids[i]<=mass :
                mass +=asteroids[i]
            else :
                f=1
        return f==0