class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen (nums.size());
        for(int i = 0; i<nums.size(); i++)
        {
            int j = target - nums[i];
            
            auto it = seen.find(j);
            if (it != seen.end()) {
                std::vector<int> ans(2);
                ans[0]=it->second-1;
                ans[1]=i;
                return ans;
            }
            seen[nums[i]]=i+1; 
        } 
        return {};
        
        
    }
};
