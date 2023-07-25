class Solution {
    public List<String> splitWordsBySeparator(List<String> words, char separator) {
        List<String> ans = new ArrayList<>();
        for (String x : words) 
        {
            int ind = 0;
            for (int i = 0; i < x.length(); i++) 
            {
                if (x.charAt(i) == separator) 
                {
                    String a = x.substring(ind, i);
                    if (!a.isEmpty()) 
                    {
                        ans.add(a);
                    }
                    ind = i + 1;
                }
            }
            String a = x.substring(ind);
            if (!a.isEmpty()) 
            {
                ans.add(a);
            }
        }
        return ans;
    }
}
