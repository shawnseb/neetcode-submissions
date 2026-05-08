class Solution {
    public String longestCommonPrefix(String[] strs) {
        int k = 0;
        while(true)
        {
            if (k >= strs[0].length()) {
                return strs[0].substring(0, k);
            }
            boolean t = true;
            
            for(int i = 1; i<strs.length; i++)
            {
                if(k>=strs[i].length())
                {
                    return strs[0].substring(0, k);
                }
                t = t & (strs[i-1].charAt(k)==strs[i].charAt(k));
                if(!t){
                    return strs[0].substring(0, k);
                }
                
            }
            k++;
            
            
        }
        
    }
}