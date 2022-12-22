class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l=[]
        for i in range(1,n+1):
            if i%3==0 and i%5 !=0:
                l.append("Fizz")
            elif i%5 ==0 and i%3 !=0:
                l.append("Buzz")
            elif i%3 ==0 and i%5==0:
                l.append("FizzBuzz")
            else :
                l.append(str(i))
        return l
