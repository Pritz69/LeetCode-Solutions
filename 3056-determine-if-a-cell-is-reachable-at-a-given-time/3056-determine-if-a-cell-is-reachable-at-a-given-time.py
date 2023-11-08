class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx==fx and sy==fy :
            if t==1 :
                return False
            return True
        ans=max(abs(fx-sx),abs(fy-sy))
        if ans <=t :
            return True
        else :
            return False