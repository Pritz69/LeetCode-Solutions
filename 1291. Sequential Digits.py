class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        st=[12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]
        ans=[]
        for x in st :
            if low <= x and x<= high :
                ans.append(x)
        return ans



class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans=[]
        s="123456789"
        l,h=len(str(low)),len(str(high))
        for i in range(l,h+1) :
            for st in range((9-i)+1) :
                num=int(s[st:st+i])
                if low <= num <= high :
                    ans.append(num)
        return ans
