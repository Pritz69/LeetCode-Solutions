class Solution:
    def numberToWords(self, num: int) -> str:
        d={1000000:"Million",1000000000:"Billion",1000:"Thousand",100:"Hundred",90:"Ninety",80:"Eighty",70:"Seventy",60:"Sixty",50:"Fifty",40:"Forty",30:"Thirty",20:"Twenty",19:"Nineteen",18:"Eighteen",17:"Seventeen",16:"Sixteen",15:"Fifteen",14:"Fourteen",13:"Thirteen",12:"Twelve",11:"Eleven",10:"Ten",9:"Nine",8:"Eight",7:"Seven",6:"Six",5:"Five",4:"Four",3:"Three",2:"Two",1:"One",0:"Zero"}
        if num==0:
            return "Zero"
        def conv(num):
            if num==0:
                return ""
            if num <= 20 :
                return d[num]
            if num < 100 :
                if num%10 == 0:
                    return d[(num//10)*10]
                else :
                    return d[(num//10)*10] +" "+ d[num%10]
            if num < 1000 :
                if num%100 == 0:
                    return d[num//100] +" Hundred"
                else :
                    return d[num//100] +" Hundred "+ conv(num%100)
            if num < 100000 :
                if num%1000 ==0 or num%10000 ==0 :
                    return conv(num//1000) + " Thousand"
                return (conv(num//1000) +" Thousand "+conv(num%1000)).strip()
            if num < 1000000 :
                if num%100000==0:
                    return d[num//100000] + " Hundred " +"Thousand"
                if ((num//1000)%100)==0 :
                    return d[num//100000] + " Hundred "  + "Thousand " +  conv(num%1000)
                return (d[num//100000] + " Hundred "  + conv((num//1000)%100)+ " Thousand " +  conv(num%1000)).strip()
            if num < 10000000 :
                if num%1000000==0 :
                    return d[num//1000000] + " Million"
                return (d[num//1000000] +" Million "+conv(num%1000000)).strip()
            if num < 100000000 :
                if num%10000000==0 :
                    return d[num//1000000] + " Million"
                return (conv(num//1000000) +" Million "+conv(num%1000000)).strip()
            if num < 1000000000 :
                if num%100000000==0 :
                    return d[num//100000000] + " Hundred" + " Million"
                return (conv(num//1000000) +" Million "+conv(num%1000000)).strip()
            if num < 10000000000 :
                if num%1000000000==0 :
                    return d[num//1000000000] + " Billion"
                return (d[num//1000000000] +" Billion "+conv(num%1000000000)).strip()
        return conv(num)
