class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        ans=[0]*n
        c=0
        op=0
        for i in range(n) :
            ans[i] += op
            c += int(boxes[i])
            op +=c
        c=0
        op=0
        for i in range(n-1,-1,-1) :
            ans[i] += op
            c += int(boxes[i])
            op +=c
        return ans