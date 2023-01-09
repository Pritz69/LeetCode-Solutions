class Solution:
    def categorizeBox(self, l: int, w: int, h: int, m: int) -> str:
        bulk=False
        heavy=False
        vol=0
        if l >= 10000 or w >= 10000 or h >= 10000 or m >= 10000 :
            bulk =True
        vol = l * w * h 
        if vol >= 1000000000 :
            bulk =True
        if m >= 100 :
            heavy =True
        if heavy and bulk :
            return ('Both')
        if not heavy and not bulk :
            return ("Neither")
        if bulk and not heavy :
            return ("Bulky")
        if heavy and not bulk :
            return ("Heavy")
