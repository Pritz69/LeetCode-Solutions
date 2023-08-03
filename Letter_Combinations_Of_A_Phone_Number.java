class Solution {
    public void backtrack(List<String> ans,String digits,Map<Character,String> h,int i,String temp)
    {
        if (temp.length()==digits.length())       // if (i==digits.length())
        {
            ans.add(temp);
            return ;
        }
        char d=digits.charAt(i);
        String s=h.get(d);
        for(int j=0;j<s.length();j++)           // for (char c:s.toCharArray())
        {
            char c=s.charAt(j);
            backtrack(ans,digits,h,i+1,temp+c);
        }
    }
    public List<String> letterCombinations(String digits) {
        Map<Character,String> h= new HashMap<>();
        h.put('2',"abc");h.put('3',"def");h.put('4',"ghi");h.put('5',"jkl");
        h.put('6',"mno");h.put('7',"pqrs");h.put('8',"tuv");h.put('9',"wxyz");
        List<String> ans=new ArrayList<>();
        if (digits.length()==0)
        {
            return ans;
        }
        backtrack(ans,digits,h,0,"");
        return ans;
    }
}
