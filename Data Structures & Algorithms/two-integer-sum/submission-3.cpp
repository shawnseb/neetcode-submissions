class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for(int i = 0; i<nums.size(); i++)
        {
            seen[nums[i]]=i; 
        } 
        for(int i = 0; i < nums.size() -1; i++)
        {
            int j = target - nums[i];
            if(seen[j] == i)
            {

            } else if (seen[j]>0) {
                std::vector<int> ans(2);
                ans[0]=i;
                ans[1]=seen[j];
                return ans;
            }
            
        }
        return {};
        
        
    }
};
