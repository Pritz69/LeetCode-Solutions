class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x = coordinates[1][0] - coordinates[0][0]
        y = coordinates[1][1] - coordinates[0][1]
        for i in range(2,len(coordinates)) :
            s = coordinates[i][1] - coordinates[0][1]
            t = coordinates[i][0] - coordinates[0][0]
            if y*t != x*s :
                return False
        return True
