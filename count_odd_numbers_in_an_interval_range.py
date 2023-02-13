class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high%2 !=0 and low%2 !=0 :
            return int(ceil((high-low)/2)) + 1
        else :
            return int(ceil((high-low)/2))
