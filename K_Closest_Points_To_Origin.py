class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort( key = lambda point: (point[0]**2 + point[1]**2) )
        
        return points[:K]
