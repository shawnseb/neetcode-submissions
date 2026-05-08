class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> keyValue = new HashMap<>();
        for(int i = 0; i<nums.length; i++)
        {
            if(keyValue.containsKey(nums[i]))
            {
                keyValue.put(nums[i], keyValue.get(nums[i])+1);
            }
            else
            {
                keyValue.put(nums[i], 1);
            }
            if(keyValue.get(nums[i])>(nums.length/2))
            {
                return nums[i];
            }

        }
        return -1;


        
    }
}