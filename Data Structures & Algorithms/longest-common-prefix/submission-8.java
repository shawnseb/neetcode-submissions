class Solution {
    public String longestCommonPrefix(String[] strs) {
        int k = 0;
        String tot = "";
        while(true)
        {
            if (k >= strs[0].length()) {
                return tot;
            }
            boolean t = true;
            
            for(int i = 1; i<strs.length; i++)
            {
                if(k>=strs[i].length() || k>=strs[i-1].length())
                {
                    return tot;
                }
                t = t & (strs[i-1].charAt(k)==strs[i].charAt(k));
                if(!t){
                    return tot;
                }
                
            }
            k++;
            tot = strs[0].substring(0, k);
            
        }
        
    }
}