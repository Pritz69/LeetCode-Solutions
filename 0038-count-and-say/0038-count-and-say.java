class Solution {
    public String countAndSay(int n) {
        String sl = "1";
        while(--n > 0){
            StringBuffer sb = new StringBuffer();
            List<Character> css = new ArrayList<>();
            for(char c : sl.toCharArray()){ 
                int csSize = css.size();
                if(csSize > 0 &&  css.get(csSize-1) !=c ){
                    sb.append(csSize);
                    sb.append(css.get(0));
                    css = new ArrayList<>();
                }
                css.add(c);
            }
            int csSize = css.size();
            if(csSize>0){
                sb.append(csSize);
                sb.append(css.get(0));
            }
            sl = sb.toString();
            System.out.println(sl);
        }
        return sl;
    }
}