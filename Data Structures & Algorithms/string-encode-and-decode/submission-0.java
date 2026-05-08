

class Solution {
    // Encodes a list of strings to a single string.
    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for (String s : strs) {
            // Format: [length] + [#] + [string]
            encoded.append(s.length()).append("#").append(s);
        }
        return encoded.toString();
    }

    // Decodes a single string back to a list of strings.
    public List<String> decode(String str) {
        List<String> res = new ArrayList<>();
        int i = 0;
        
        while (i < str.length()) {
            // 1. Find the delimiter to know how long the length is
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            
            // 2. Extract the length and move pointer past the '#'
            int length = Integer.parseInt(str.substring(i, j));
            i = j + 1;
            
            // 3. Extract the actual string based on that length
            res.add(str.substring(i, i + length));
            
            // 4. Move pointer to the start of the next encoded block
            i += length;
        }
        return res;
    }
}