class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs==null||strs.length==0)
        {
            return "";
        }
        String prefix = "";
        char[] index = strs[minLengthIndex(strs)].toCharArray();
        for(int i =0; i<index.length; i++)
        {
            char firstLetter=index[i];
            for(int j=0; j<strs.length; j++)
            {
                char otherLetter=strs[j].charAt(i);
                if(firstLetter!=otherLetter)
                {
                    return prefix;
                }
            }
            prefix+=index[i];
        }
        return prefix;
    }
    public int minLengthIndex(String[] strs)
    {
        int min = strs[0].length();
        int minIndex = 0;
        for(int j=0; j<strs.length; j++)
        {
            if(strs[j].length()< min)
            {
                min=strs[j].length();
                minIndex=j;
            }
            
        }
        return minIndex;
    }
}