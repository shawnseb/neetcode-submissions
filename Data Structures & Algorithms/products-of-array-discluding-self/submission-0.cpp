class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int zeros = 0;
        for(int i = 0; i < nums.size(); i++)
        {
            if(nums[i]!=0)
            {
                product *= nums[i];
            } else {
                zeros++;
            }
        }
        
        vector<int> ans;
        if(zeros>1)
        {
            vector<int> edge(nums.size());
            return edge;
        }
        ans.reserve(nums.size());
        for(int i = 0; i < nums.size(); i++)
        {
            if(nums[i]==0)
            {
                ans.push_back(product);
            } else if(zeros>0){
                ans.push_back(0);
            } else {
                ans.push_back(product/(nums[i]));
            }
        }
        return ans;

    }
};
