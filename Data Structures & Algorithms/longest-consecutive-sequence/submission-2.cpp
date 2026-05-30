class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size()==0)
        {
            return 0;
        }
        unordered_set<int> seen(nums.size());
        for(short i = 0; i<(short)nums.size(); i++)
        {
            seen.insert(nums[i]);
        }
        short max = 0;;
        for(short i = 0; i <(short)nums.size(); i++)
        {
            int prev = nums[i];
            short track = 0;
            if(max > ((short)nums.size()) - i)
            {
                std::cout<<("out");
                break;
            }
            while(seen.find(prev+1)!=seen.end())
            {
                track++;
                prev++;
            }
            if(track>max)
            {
                max=track;
            }
        }
        return max + 1;
        
    }
};
