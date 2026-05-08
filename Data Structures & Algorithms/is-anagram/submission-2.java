class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())
        {
            return false;
        }
        HashMap<String, Integer> map = new HashMap<>();
        for(int i = 0; i<s.length(); i++)
        {
            String f = s.substring(i, i+1);
            map.put(f, map.getOrDefault(f, 0) +1);
        }
        HashMap<String, Integer> map2 = new HashMap<>();
        for(int i = 0; i<s.length(); i++)
        {
            String f = t.substring(i, i+1);
            map2.put(f, map2.getOrDefault(f, 0) +1);
            if(map2.get(f)>map.getOrDefault(f,0))
            {
                return false;
            }
        }
        return true;

    }
}
