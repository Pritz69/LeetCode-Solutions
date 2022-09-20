class Solution:
    def converter(mapp,s):
        n = 0
        for i in s:
            n = n*10 + mapp[i]
        return n
            
    def addStrings(self, num1: str, num2: str) -> str:
        
        mapp = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        
        return str(Solution.converter(mapp,num1) + Solution.converter(mapp,num2))
