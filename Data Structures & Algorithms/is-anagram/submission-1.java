class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())
        {
            return false;
        }
        ArrayList<String> list = new ArrayList<>();
        for(int i=0; i<s.length(); i++)
        {
            list.add(s.substring(i,i+1));
            
        }
        for(int i=0; i<t.length(); i++)
        {
            if(list.contains(t.substring(i,i+1)))
            {
                list.remove(t.substring(i,i+1));
                
            }else{
                return false;
            }
        }
        return true;
    }
}
