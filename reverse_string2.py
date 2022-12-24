class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = (a[i:i+k])[::-1]
        return "".join(a)
