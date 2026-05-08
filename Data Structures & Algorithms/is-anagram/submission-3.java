class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())
        {
            return false;
        }
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i<s.length(); i++)
        {
            char f = s.charAt(i);
            map.put(f, map.getOrDefault(f, 0) +1);
        }
        HashMap<Character, Integer> map2 = new HashMap<>();
        for(int i = 0; i<s.length(); i++)
        {
            char f = t.charAt(i);
            map2.put(f, map2.getOrDefault(f, 0) +1);
            if(map2.get(f)>map.getOrDefault(f,0))
            {
                return false;
            }
        }
        return true;

    }
}
