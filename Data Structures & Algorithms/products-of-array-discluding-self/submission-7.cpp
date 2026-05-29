class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        auto init = []() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    return 0;
}();
        int front = 1;
        int back = 1;
        int n = nums.size();
        vector<int> backs (nums.size());
        for(int i = n-1; i>-1; i--)
        {
            backs[i]=back;
            back*=nums[i];
        }
        for(int i = 0; i < n; i++)
        {
            backs[i]=front*backs[i];
            back = 1;
            front*=nums[i];
        }
        
        return backs;

    }
};
