class Solution {
    public int compress(char[] chars) {
        int index=0;
        int i=0;
        while (i< chars.length)
        {
            int j=i;
            while (j< chars.length && chars[j]==chars[i])
            {
                j ++;
            }
            chars[index++]=chars[i];
            if (j-i >1) 
            {
                String c= j-i +"";
                for (char x:c.toCharArray())
                {
                    chars[index++]=x;
                }
            }
            i=j;
        }
        return index;
    }
}
