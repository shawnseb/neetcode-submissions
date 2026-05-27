class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for(int i = 0; i<nums.size(); i++)
        {
            int x = nums[i];
            if(seen.count(x))
            {
               return true;  
            }
            seen.insert(x);
        }
        return false;
    }
};