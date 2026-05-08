class Solution {
    public int removeElement(int[] nums, int val) {
        Queue<Integer> index = new LinkedList<>();
        int ans = 0;
        for(int i = 0; i<nums.length; i++)
        {
            if(nums[i]==val)
            {
                index.add(i);
                
            } else {
                ans++;
                if(index.isEmpty())
                {

                } else{
                    nums[index.poll()] = nums[i];
                    index.add(i);
                }

            }

        }
        return ans;
        
    }
}