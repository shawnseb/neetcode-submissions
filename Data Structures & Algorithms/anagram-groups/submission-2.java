class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs == null || strs.length == 0) return new ArrayList<>();
        
        Map<String, List<String>> map = new HashMap<>();
        
        for (String s : strs) {
            // Use a fixed-size array since we know it's a-z
            int[] count = new int[26];
            for (char c : s.toCharArray()) count[c - 'a']++;
            
            // Generate a unique string key: e.g., "[1, 0, 2, 0...]"
            String key = Arrays.toString(count);
            
            // Professional way to handle the "list exists or create new" logic
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(s);
        }
        
        return new ArrayList<>(map.values());
    }
}