class Solution {
    public String sortVowels(String s) {
        ArrayList<Character> v = new ArrayList<>();
        ArrayList<Character> c = new ArrayList<>();
        for (char x : s.toCharArray()) {
            if ("AEIOUaeiou".contains(String.valueOf(x))) {
                v.add(x);
            } else {
                c.add(x);
            }
        }
        Collections.sort(v);
        ArrayList<Character> ans = new ArrayList<>();
        int i = 0, j = 0;
        for (char x : s.toCharArray()) 
        {
            if ("AEIOUaeiou".contains(String.valueOf(x))) 
            {
                ans.add(v.get(i));
                i++;
            } else 
            {
                ans.add(c.get(j));
                j++;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char x : ans) 
        {
            sb.append(x);
        }
        return sb.toString();
    }
}
/* PYTHON SOLUTION
  class Solution:
    def sortVowels(self, s: str) -> str:
        v=[]
        c=[]
        for x in s :
            if x in "AEIOUaeiou" :
                v.append(x)
            else :
                c.append(x)
        v.sort()
        ans=[]
        i,j=0,0
        for k,x in enumerate(s) :
            if x in "AEIOUaeiou" :
                ans.append(v[i])
                i +=1
            else :
                ans.append(c[j])
                j +=1
        return ''.join(ans)
*/
