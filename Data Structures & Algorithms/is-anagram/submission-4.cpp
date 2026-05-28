class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length())
        {
            return false;
        }
        unordered_map<char, int> seen;
        for(int i = 0; i < s.length(); i++)
        {
            seen[s[i]]++;
        }
        for(int i = 0; i < t.length(); i++)
        {
            if(seen[t[i]]==0)
            {
                return false;
            }
            seen[t[i]]--;
        }
        return true;
    }
    
};
