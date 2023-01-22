class Solution {
    boolean isPal(String s,int st,int end)
    {
        while(st<=end)
        {
            if(s.charAt(st++)!=s.charAt(end--))
            {
                return false;
            }
        }
        return true;
    }
    public void backtrack(String s,int ind,List<String> path,List<List<String>> res)
    {
        if (ind==s.length())
        {
            res.add(new ArrayList<>(path));
        }
        for(int i=ind;i<s.length();i++)
        {
            if(isPal(s,ind,i))
            {
                path.add(s.substring(ind,i+1));
                backtrack(s,i+1,path,res);
                path.remove(path.size()-1);
            }
        }
    }
    public List<List<String>> partition(String s)
    {
       List<List<String>> res= new ArrayList<>();
       List<String> path=new ArrayList<>();
       backtrack(s,0,path,res);
       return res;
    }
}
