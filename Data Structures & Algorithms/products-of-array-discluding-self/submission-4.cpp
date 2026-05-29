class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int front = 1;
        int back = 1;
        int j = 0;
        vector<int> backs (nums.size());
        for(int i = nums.size()-1; i>-1; i--)
        {
            backs[i]=back;
            back*=nums[i];
        }
        for(int i = 0; i < nums.size(); i++)
        {
            backs[i]=front*backs[i];
            back = 1;
            front*=nums[i];
        }
        
        return backs;

    }
};
