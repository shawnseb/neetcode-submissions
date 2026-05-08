class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<HashMap<Character, Integer>, List<String>> set = new HashMap<>();
        for(int i = 0; i < strs.length; i++)
        {
            HashMap<Character, Integer> small = new HashMap<>();
            for(char c: strs[i].toCharArray())
            {
                small.put(c, small.getOrDefault(c, 0) + 1);
            }
            if(set.containsKey(small))
            {
                List<String> list = set.get(small);
                list.add(strs[i]);
            } else {
                List<String> list = new ArrayList<>();
                list.add(strs[i]);
                set.put(small, list);
            }
        }
        List<List<String>> answer = new ArrayList<>();
        for(HashMap<Character, Integer> c : set.keySet())
        {
            answer.add(set.get(c));
        }
        return answer;
        
    }
}
