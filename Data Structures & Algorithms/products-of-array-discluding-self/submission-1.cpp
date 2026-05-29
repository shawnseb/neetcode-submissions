class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int front = 1;
        int back = 1;
        int j = 0;
        vector<int> ans (nums.size());
        for(int i = 0; i < nums.size(); i++)
        {
            while(j<nums.size())
            {
                if(i>j)
                {
                    front*=nums[j];
                    
                } else if(i<j)
                {
                    back*=nums[j];
                }
                j++;
            }
            ans[i]=front*back;
            j=i+1;
            back = 1;
            front*=nums[i];
        }
        
        return ans;

    }
};
