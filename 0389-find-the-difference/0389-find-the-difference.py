class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d={}
        for i in t :
            d[i]=d.get(i,0) +1
        for i in s :
            d[i]=d.get(i,0) -1
        for x in d :
            if d[x]==1 :
                return x
        return 0