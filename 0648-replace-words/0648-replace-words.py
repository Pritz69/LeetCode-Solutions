class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        s=set(dictionary)
        ans=[]
        for w in sentence.split(" ") :
            wo=""
            f=0
            for i in range(len(w)) :
                wo=wo+w[i]
                if wo in s :
                    f=1
                    ans.append(wo)
                    break
            if f==0 :
                ans.append(w)
        return ' '.join(ans)